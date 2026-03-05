from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


def save_image(file):
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return path


# ---------- Improved Tooth Detection ----------
def detect_teeth(path):

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    # Reduce noise
    blur = cv2.GaussianBlur(gray,(7,7),0)

    # Detect edges
    edges = cv2.Canny(blur,40,120)

    # Connect structures
    kernel = np.ones((5,5),np.uint8)
    edges = cv2.dilate(edges,kernel,iterations=2)

    contours,_ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    teeth = []

    for c in contours:

        area = cv2.contourArea(c)

        if 2000 < area < 20000:

            x,y,w,h = cv2.boundingRect(c)

            ratio = h / float(w)

            if 0.6 < ratio < 2.5:
                teeth.append((x,y,w,h))

    teeth = sorted(teeth, key=lambda t:t[0])

    return img, teeth


# ---------- Segmentation ----------
@app.route("/segment", methods=["POST"])
def segment():

    file = request.files["image"]
    path = save_image(file)

    img, teeth = detect_teeth(path)

    for (x,y,w,h) in teeth:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    output = "segmentation.png"
    out_path = os.path.join(RESULT_FOLDER,output)

    cv2.imwrite(out_path,img)

    return jsonify({
        "result":f"{len(teeth)} teeth detected",
        "image":"/results/"+output
    })


# ---------- Tooth Numbering ----------
@app.route("/tooth_number", methods=["POST"])
def tooth_number():

    file = request.files["image"]
    path = save_image(file)

    img, teeth = detect_teeth(path)

    for i,(x,y,w,h) in enumerate(teeth):

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

        cv2.putText(
            img,
            str(i+1),
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,0,0),
            2
        )

    output = "numbering.png"
    out_path = os.path.join(RESULT_FOLDER,output)

    cv2.imwrite(out_path,img)

    return jsonify({
        "result":"Teeth numbered successfully",
        "image":"/results/"+output
    })


# ---------- Missing Tooth Detection ----------
@app.route("/missing_tooth", methods=["POST"])
def missing_tooth():

    file = request.files["image"]
    path = save_image(file)

    img, teeth = detect_teeth(path)

    missing = False

    for i in range(len(teeth)-1):

        x1 = teeth[i][0]
        x2 = teeth[i+1][0]

        gap = x2 - x1

        if gap > 120:

            missing = True

            cv2.putText(
                img,
                "Missing Tooth",
                (x1+20,60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                3
            )

    for (x,y,w,h) in teeth:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    output = "missing.png"
    out_path = os.path.join(RESULT_FOLDER,output)

    cv2.imwrite(out_path,img)

    return jsonify({
        "result":"Possible missing tooth detected" if missing else "No missing tooth detected",
        "image":"/results/"+output
    })


# ---------- Implant Classification ----------
@app.route("/implant_classify", methods=["POST"])
def implant_classify():

    file = request.files["image"]
    path = save_image(file)

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    variance = np.var(gray)

    if variance > 900:
        status = "Implant appears Normal"
        color = (0,255,0)

    elif variance > 500:
        status = "Possible cavity detected"
        color = (0,0,255)

    else:
        status = "Filling detected"
        color = (255,0,0)

    cv2.putText(
        img,
        status,
        (40,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    output = "implant.png"
    out_path = os.path.join(RESULT_FOLDER,output)

    cv2.imwrite(out_path,img)

    return jsonify({
        "result":status,
        "image":"/results/"+output
    })


# ---------- Serve Images ----------
@app.route("/results/<filename>")
def results(filename):
    return send_from_directory(RESULT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
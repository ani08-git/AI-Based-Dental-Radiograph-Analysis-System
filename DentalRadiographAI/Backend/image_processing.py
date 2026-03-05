import cv2
import numpy as np


def analyze_xray(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    boxes = [cv2.boundingRect(c) for c in contours]

    # sort teeth from left to right
    boxes = sorted(boxes, key=lambda b: b[0])

    tooth_count = len(boxes)

    anomalies = []

    for i, (x, y, w, h) in enumerate(boxes):

        tooth_number = i + 1

        tooth_region = gray[y:y+h, x:x+w]

        mean_intensity = np.mean(tooth_region)

        # classification rules
        if mean_intensity < 80:
            label = "Cavity"
            color = (0,0,255)

        elif mean_intensity > 200:
            label = "Filling"
            color = (255,0,0)

        elif h > 120:
            label = "Impacted"
            color = (0,255,255)

        else:
            label = "Normal"
            color = (0,255,0)

        # draw bounding box
        cv2.rectangle(image, (x,y), (x+w,y+h), color, 2)

        # tooth number
        cv2.putText(
            image,
            f"{tooth_number}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2
        )

        # classification label
        cv2.putText(
            image,
            label,
            (x, y+h+15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            color,
            1
        )

        # simple bone loss detection
        bone_region = gray[y+h:y+h+20, x:x+w]

        if bone_region.size > 0:
            bone_density = np.mean(bone_region)

            if bone_density < 70:
                anomalies.append(f"Bone loss near tooth {tooth_number}")

    result_data = {
        "detected_teeth": tooth_count,
        "anomalies": anomalies
    }

    return result_data, image
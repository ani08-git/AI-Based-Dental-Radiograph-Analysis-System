# AI-Based-Dental-Radiograph-Analysis-System
## Overview

The **AI-Based Dental Radiograph Analysis System** is a web-based application that analyzes panoramic dental X-ray (OPG) images using computer vision techniques. The system allows users to upload dental radiographs and perform automated analysis such as **tooth segmentation, tooth numbering, missing tooth detection, and implant classification**.

The backend uses **Python, Flask, and OpenCV** for image processing, while the frontend uses **HTML, CSS, and JavaScript** to provide an interactive interface where the results are visualized directly on the uploaded X-ray image.

This project demonstrates how computer vision can assist in **basic dental image analysis and visualization**.

---

# Features

### 1. Dental X-ray Upload

Users can upload panoramic dental X-ray images (OPG) through the web interface.

### 2. Image Preview

The uploaded X-ray is previewed before analysis.

### 3. Tooth Segmentation

Detects tooth-like regions in the X-ray using image processing techniques.

### 4. Tooth Numbering

Labels detected teeth in sequential order.

### 5. Missing Tooth Detection

Detects potential gaps between teeth indicating missing or impacted teeth.

### 6. Implant Classification

Analyzes tooth regions and classifies implant status.

### 7. Annotated Image Output

The processed X-ray image is returned with bounding boxes and labels showing detected regions.

---

# Technologies Used

## Backend

* **Python**
* **Flask** – Web server and API
* **Flask-CORS** – Cross-origin requests
* **OpenCV** – Image processing
* **NumPy** – Numerical operations

## Frontend

* **HTML**
* **CSS**
* **JavaScript**
* **Fetch API** for backend communication

## Tools

* **Git & GitHub** for version control
* **VS Code** for development

---

# Project Structure

```
AI-Based-Dental-Radiograph-Analysis-System
│
├── Backend
│   ├── app.py
│   ├── image_processing.py
│   ├── report_generator.py
│   ├── test_upload.py
│   ├── uploads
│   └── results
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# How the System Works

1. The user uploads a dental X-ray image from the frontend.
2. The image is sent to the Flask backend via API.
3. OpenCV processes the image to detect tooth regions.
4. The system performs the selected analysis:

   * Segmentation
   * Tooth numbering
   * Missing tooth detection
   * Implant classification
5. The processed image with annotations is returned to the frontend and displayed.

---

# Installation

## 1. Clone the Repository

```
git clone https://github.com/ani08-git/AI-Based-Dental-Radiograph-Analysis-System.git
cd AI-Based-Dental-Radiograph-Analysis-System
```

---

## 2. Create a Virtual Environment

```
python -m venv .venv
```

Activate it:

### Windows

```
.venv\Scripts\activate
```

### Linux / Mac

```
source .venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 – Start the Backend Server

Navigate to the backend folder:

```
cd Backend
```

Run the Flask server:

```
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

## Step 2 – Open the Frontend

Navigate to the frontend folder and open:

```
frontend/index.html
```

Open it in any web browser.

# Using the System

1. Upload a dental X-ray image.
2. Choose one of the analysis options:

   * Segmentation
   * Tooth Numbering
   * Missing Tooth Detection
   * Implant Classification
3. The system processes the image and displays the annotated result.

# Example Capabilities

* Highlight tooth regions
* Label detected teeth
* Detect potential missing teeth
* Provide implant status feedback

# Limitations

* The system currently uses **rule-based computer vision techniques**.
* Detection accuracy may vary depending on image quality.
* For real-world dental diagnostics, **deep learning models (YOLO, U-Net, Mask R-CNN)** would provide better accuracy.

# Future Improvements

* Deep learning-based tooth detection
* Automatic cavity detection
* Dental report generation
* Cloud deployment
* Support for multiple radiograph types

# License

This project is developed for **educational and research purposes**.


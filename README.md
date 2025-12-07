# face-recognition_opencv


# face-recognition_opencv

> Simple face detection & basic recognition demo using **Python** and **OpenCV**.
> Live webcam feed, draws bounding boxes around detected faces, and exits when you press **`q`**.

---

## Table of Contents

* [About](#about)
* [Features](#features)
* [Demo](#demo)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Project structure](#project-structure)
* [How it works (brief)](#how-it-works-brief)
* [Improving accuracy / Next steps](#improving-accuracy--next-steps)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)

---

# About

This repository is a compact example that demonstrates how to detect (and in a basic way *recognize*) faces using OpenCV in Python. It opens your webcam, processes each frame to detect faces (using a Haar Cascade), draws rectangles around detected faces, and allows you to quit the program by pressing **`q`**.

This README is written to be copy-paste ready for a GitHub repository.

---

# Features

* Real-time face detection from webcam.
* Uses classic OpenCV face detector (Haar Cascade).
* Minimal, easy-to-understand Python code for learning and extension.
* Press **`q`** to quit the live window and stop the program.

---

# Demo

> Run the script and you will see a live window showing the webcam feed. Detected faces are highlighted with rectangles. Press `q` to close.

*(If you want, add a screenshot or GIF named `demo.gif` or `screenshot.png` in the repo and reference it here: `![Demo](./demo.gif)`.)*

---

# Requirements

* Python 3.6+
* Packages in `requirements.txt` (typical minimums below)

Typical packages:

```text
opencv-python
numpy
```

> If a `requirements.txt` exists in the repository, prefer installing from it.

---

# Installation

```bash
# 1. Clone the repository
git clone https://github.com/ArianGhaderi99/face-recognition_opencv.git
cd face-recognition_opencv

# 2. (Optional but recommended) Create & activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
# or install minimum packages
pip install opencv-python numpy
```

---

# Usage

```bash
# from repository root
python face_recognition.py
```

* The script will open your default webcam (`cv2.VideoCapture(0)`).
* A window will appear showing the camera feed with detected faces boxed.
* Press **`q`** in the window (or while the terminal has focus) to exit the program cleanly.

---

# Project structure

```
face-recognition_opencv/
├─ face_recognition.py                 # main script (webcam capture + detection)
├─ haarcascade_frontalface_default.xml  # Haar Cascade file used for detection
├─ requirements.txt                     # python packages (if present)
├─ README.md                            # (this file)
└─ (optional) demo.gif / screenshot.png # optional demo media to display in README
```

> If your repo uses different filenames, update the commands above to match.

---

# How it works (brief)

1. **Open webcam**: `cv2.VideoCapture(0)` reads frames in a loop.
2. **Convert to grayscale**: Haar cascades work faster/more reliably on gray frames.
3. **Detect faces**: `cascade.detectMultiScale(...)` returns bounding boxes for each detected face.
4. **Draw rectangles**: Draw a rectangle around each detection and optionally show labels.
5. **Exit**: The loop listens for keyboard input and breaks when **`q`** is pressed; camera and windows are released/destroyed.

This repository uses a traditional computer-vision approach (Haar Cascades). It is compact and well suited for learning; modern projects often use deep learning models (MTCNN, dlib, FaceNet, etc.) for higher accuracy.

---

# Improving accuracy / Next steps

If you want to expand this project toward robust face recognition, consider:

* Replacing Haar Cascade with modern detectors (MTCNN, RetinaFace).
* Using pretrained face embeddings (FaceNet, ArcFace) to generate embeddings, then train a classifier (SVM / KNN) for identification.
* Adding a small GUI (Tkinter, PySimpleGUI) for dataset collection and training.
* Adding lighting normalization, face alignment, and data augmentation for better results.
* Using `cv2.VideoCapture()` index or video file input for different camera sources.

---

# Troubleshooting

* **Camera doesn't open**: Make sure your webcam is connected and not used by another application. Try different indices like `cv2.VideoCapture(1)`.
* **Black screen or no detections**: Check lighting and camera position; Haar cascades work poorly in low light or large pose variations.
* **Import errors**: Ensure you activated the virtual environment and installed dependencies (`pip install -r requirements.txt`).
* **Slow performance**: Try resizing frames before detection (e.g., downscale by a factor), or use a faster detector.

---

# Contributing

Contributions, bug reports, and improvements (e.g., adding an example for training a simple recognizer, including a demo gif, or switching to a modern face detector) are welcome!

Steps:

1. Fork the repo
2. Create a new branch: `git checkout -b feature/my-feature`
3. Commit your changes and push: `git push origin feature/my-feature`
4. Open a Pull Request and describe your changes

---

# License

This project is licensed under the **MIT License** — feel free to reuse and modify. Add a `LICENSE` file with the MIT text if it is not present.

---

# A final note

If you'd like, I can also:

* Produce a polished **two-column English + Persian** README,
* Generate a **GIF screenshot** of the script in action to embed in the README, or
* Provide a **minimal example** that adds a small recognizer (collect faces → train a simple classifier → run recognition).

Tell me which of those you'd like and I'll produce the files ready to paste into the repository.


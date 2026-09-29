# 👁️ Computer Vision & Real-Time Tracking Suite

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.5-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.11-orange?logo=google&logoColor=white)](https://developers.google.com/mediapipe)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/)

A modular, real-time Computer Vision suite built with **Python**, **OpenCV**, and Google's **MediaPipe**. This repository features standalone modules and applications for face detection, 468-point facial mesh tracking, hand landmark tracking, full-body pose estimation with joint angle calculations, and gesture-based hardware control.

---

## 🌟 Modules & Features

### 1. ✋ Hand Tracking & Gesture Control
* **[`HandTrackingModule.py`](HandTrackingModule.py)**: Modular class detecting 21 hand landmarks per hand, returning normalized and pixel coordinates.
* **[`VolumeHandControl.py`](VolumeHandControl.py)**: Real-time system audio volume controller mapped to the euclidean distance between thumb and index finger tips using **PyCaw** (Python Core Audio Windows Library). Features visual volume bars and percentage readouts.

### 2. 👤 Face Detection & 468-Point Face Mesh
* **[`FaceDetectionModule.py`](FaceDetectionModule.py)**: High-speed face detector with custom corner-accented bounding boxes and confidence score overlay.
* **[`FaceMeshModule.py`](FaceMeshModule.py)**: Tracks 468 3D facial landmarks in real-time, capable of tracking eye blinks, facial expressions, and head tilt.

### 3. 🏃 Full-Body Pose Estimation & Biometrics
* **[`PoseTrackingModule.py`](PoseTrackingModule.py)**: Tracks 33 full-body landmarks. Includes vector-math angle calculation across 3 joints (e.g. shoulder-elbow-wrist or hip-knee-ankle) — ideal for fitness rep counting and posture correction.

---

## 📁 Repository Structure

```text
TrackingProject/
├── FaceDetectionModule.py   # Reusable face detector class
├── FaceMeshModule.py        # 468-point facial mesh module
├── FaceMeshBasics.py        # Minimal face mesh demo
├── FaceTrackingMin.py       # Minimal face detection demo
├── HandTrackingModule.py    # Reusable 21-point hand tracking class
├── HandtrackingMin.py       # Minimal hand tracking demo
├── PoseTrackingModule.py    # Reusable 33-point pose estimation class
├── PoseEstimationMin.py     # Minimal pose estimation demo
├── VolumeHandControl.py     # Real-time gesture volume controller (PyCaw)
├── FaceVideos/              # Directory for sample face test videos (.gitkeep)
├── PoseVideos/              # Directory for sample pose test videos (.gitkeep)
├── requirements.txt         # Project dependencies
└── .gitignore               # Ignored virtualenvs, binaries & caches
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.8 to 3.11 recommended
* A working webcam for real-time applications

### 2. Installation
```bash
# Clone the repository
git clone <YOUR_REPO_URL>
cd TrackingProject

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Running Applications

#### Gesture-Controlled Audio Volume:
```bash
python VolumeHandControl.py
```
* Pinch thumb and index finger together to lower volume; spread them apart to increase volume.

#### Hand Tracking:
```bash
python HandTrackingModule.py
```

#### Pose Estimation:
```bash
python PoseTrackingModule.py
```

#### Face Mesh:
```bash
python FaceMeshModule.py
```

---

## 👨‍💻 Author

**Himanshu Patil**
* GitHub: [@HimanshuPatil2001](https://github.com/HimanshuPatil2001)

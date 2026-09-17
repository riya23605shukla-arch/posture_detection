# 🧍 Posture Correction System

An AI-powered **real-time posture detection and correction system** that uses a webcam to analyze a person's body posture and identify whether the posture is **correct or incorrect**.

The system uses **Computer Vision, MediaPipe Pose, OpenCV, and Hugging Face** to process webcam input, detect body landmarks, analyze posture, and provide real-time feedback to the user.

---

## 📌 Project Overview

Poor posture is a common problem caused by prolonged sitting, studying, working on computers, or using mobile devices. Maintaining an incorrect posture for long periods can lead to discomfort and long-term musculoskeletal problems.

The **Posture Correction System** provides a simple computer-vision-based solution for monitoring posture in real time.

The application captures video through a webcam and detects important body landmarks such as the:

* Head
* Shoulders
* Neck
* Spine
* Hips

These landmarks are analyzed to determine whether the user's posture falls within the defined range for a **correct posture**.

If an incorrect posture is detected, the system provides visual feedback so that the user can adjust their position.

---

## ✨ Features

### 🎥 Real-Time Posture Detection

The system continuously processes webcam frames and analyzes the user's posture in real time.

### 🦴 Body Landmark Detection

MediaPipe Pose is used to identify important human body landmarks.

### ⚠️ Incorrect Posture Detection

The system detects deviations from the defined correct-posture conditions.

### ✅ Correct Posture Identification

When the detected body alignment satisfies the required conditions, the system indicates that the posture is correct.

### 💻 Webcam-Based

No specialized hardware is required. A normal laptop or external webcam can be used.

### 🤖 AI & Computer Vision

The project combines computer vision and machine-learning-based pose estimation to analyze human posture.

### 📊 Visual Feedback

The detected posture status is displayed directly on the webcam interface.

### 🔄 Continuous Monitoring

The system can monitor posture continuously while the application is running.

---

# 🛠️ Technologies Used

| Technology         | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| **Python**         | Core programming language                      |
| **OpenCV**         | Webcam access and image/video processing       |
| **MediaPipe Pose** | Human pose and body landmark detection         |
| **Hugging Face**   | AI/ML model and ecosystem integration          |
| **NumPy**          | Numerical calculations and landmark processing |

---

# 🧠 How the System Works

The system follows a simple computer-vision pipeline:

```text
                ┌─────────────────┐
                │     Webcam      │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │   Video Frame   │
                │    Capture      │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │    OpenCV       │
                │ Image Processing │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ MediaPipe Pose  │
                │ Landmark Detect.│
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Posture Feature │
                │    Analysis     │
                └────────┬────────┘
                         ↓
              ┌──────────┴──────────┐
              ↓                     ↓
       ┌──────────────┐      ┌──────────────┐
       │    Correct   │      │   Incorrect  │
       │    Posture   │      │    Posture   │
       └──────────────┘      └──────────────┘
              ↓                     ↓
       ┌──────────────┐      ┌──────────────┐
       │ Positive     │      │ Correction   │
       │ Feedback     │      │ Feedback     │
       └──────────────┘      └──────────────┘
```

---

# 🔍 Posture Detection Process

## 1. Webcam Input

The webcam captures the user's live video.

OpenCV is responsible for accessing the webcam and reading individual frames.

```python
cap = cv2.VideoCapture(0)
```

Each frame is processed individually.

---

## 2. Image Processing

The captured frame is converted into the format required by the pose detection pipeline.

OpenCV is used for:

* Video capture
* Frame processing
* Image conversion
* Drawing results
* Displaying feedback

---

## 3. Pose Detection

MediaPipe Pose identifies human body landmarks from the webcam frame.

The detected landmarks can include points such as:

```text
        Nose
         ●
        / \
       ●   ●
   Shoulder Shoulder
       |   |
       |   |
       ●   ●
       Hip  Hip
```

Each landmark contains positional information that can be used for posture analysis.

---

## 4. Landmark Analysis

The detected body landmarks are used to evaluate body alignment.

Depending on the implementation, the system can analyze:

* Shoulder alignment
* Head position
* Neck alignment
* Torso orientation
* Hip alignment
* Relative angles between body landmarks
* Distance between important body points

These measurements are compared with predefined posture conditions.

---

## 5. Posture Classification

After analyzing the detected landmarks, the system determines the posture status.

The result can be classified as:

### 🟢 Correct Posture

The detected body alignment satisfies the defined posture conditions.

### 🔴 Incorrect Posture

One or more body alignment conditions are outside the acceptable range.

The corresponding status is displayed on the screen.

---

# 📂 Project Structure

A typical project structure is:

```text
posturecorrection/
│
├── main.py
│
├── requirements.txt
│
├── README.md
│
├── models/
│   └── ...
│
├── utils/
│   └── ...
│
└── other supporting files
```

### `main.py`

The main Python program responsible for:

* Opening the webcam
* Processing video frames
* Detecting body landmarks
* Performing posture analysis
* Displaying posture feedback

### `requirements.txt`

Contains the Python libraries required to run the project.

### Supporting Files

Additional files can contain:

* Utility functions
* Model configuration
* Posture detection logic
* Helper functions
* AI/ML model files

---

# ⚙️ Installation

## Prerequisites

Before running the project, make sure you have:

* Python 3.x
* A working webcam
* Internet connection for installing dependencies
* Windows/Linux/macOS

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/riya23605shukla-arch/posturecorrection.git
```

Move into the project directory:

```bash
cd posturecorrection
```

---

## Step 2 — Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## Step 3 — Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

If a requirements file is not available, the core dependencies may include:

```bash
pip install opencv-python mediapipe numpy
```

Additional dependencies should be installed according to the project's implementation.

---

# ▶️ How to Run

After installing all dependencies, run:

```bash
python main.py
```

The webcam should open and begin detecting the user's posture.

Position yourself in front of the camera so that the relevant body landmarks are visible.

---

# 🖥️ Expected Output

Once the program starts:

1. The webcam captures live video.
2. The system detects the user's body.
3. MediaPipe identifies body landmarks.
4. The posture analysis logic evaluates body alignment.
5. The system displays the detected posture status.

Example:

```text
+--------------------------------------+
|                                      |
|          Live Webcam Feed            |
|                                      |
|             🧍                       |
|            /|\                       |
|            / \                       |
|                                      |
|       POSTURE: CORRECT               |
|                                      |
+--------------------------------------+
```

For an incorrect posture, the application can display an appropriate warning or correction message.

---

# 🎯 Use Cases

The Posture Correction System can be useful in several scenarios.

###  Students

Students who spend several hours studying at a desk can use the system to monitor their sitting posture.

###  Developers

Developers and software professionals who spend long periods in front of computers can use it for posture awareness.

###  Work From Home

The system can be used during home-based work or study sessions.

###  Office Work

Employees can use webcam-based posture monitoring to become more aware of their sitting position.

###  Fitness & Exercise

The underlying pose-detection approach can potentially be extended to monitor body alignment during certain exercises.

---

#  Technical Concepts

This project demonstrates several important concepts in Artificial Intelligence and Computer Vision.

### Computer Vision

The system processes visual information from a webcam to understand the position of a person's body.

### Human Pose Estimation

Pose estimation identifies important points on the human body from an image or video frame.

### Landmark Detection

Instead of treating the entire image as one object, the system extracts meaningful body landmarks and uses their coordinates for analysis.

### Geometric Analysis

Body alignment can be analyzed using:

* Coordinates
* Distances
* Slopes
* Angles
* Relative positions

For example, the angle between three landmarks can be calculated using:

```text
        A
       /
      /
     B────────C
```

The angle at point `B` can provide information about the orientation of the body.

---

#  Future Improvements

The current system can be extended with additional features.

##  Voice Alerts

Add voice notifications such as:

```text
"Please correct your posture."
```

when incorrect posture continues for a specific duration.

---

##  Posture Monitoring Timer

Track how long a user maintains an incorrect posture.

For example:

```text
Incorrect posture detected
Duration: 00:15
```

This can prevent the system from reacting to very short or accidental movements.

---

##  Posture Statistics

Store posture information and display statistics such as:

```text
Daily Posture Report

Correct Posture      78%
Incorrect Posture    22%

Total Monitoring     2h 15m
```

---

##  Mobile/Web Application

The posture detection system could be extended into a web or mobile application, allowing users to access posture monitoring from different devices.

---

##  Improved ML Classification

A machine-learning classifier could be trained using posture landmarks to distinguish between multiple posture categories.

For example:

```text
Good Posture
     │
     ├── Upright Sitting
     │
     └── Correct Standing


Poor Posture
     │
     ├── Slouching
     ├── Forward Head
     └── Uneven Shoulder
```

---

##  Personalized Posture Analysis

Future versions could allow users to create personalized posture thresholds based on their body proportions and preferred working position.

---

#  Limitations

The system's accuracy depends on several factors:

* Webcam quality
* Lighting conditions
* Camera position
* User distance from the camera
* Visibility of body landmarks
* Body orientation
* Clothing and background
* Defined posture thresholds

The system is intended for **posture awareness and educational purposes** and should not be considered a medical diagnostic tool.

---

#  Privacy

The application is designed around webcam-based processing.

Users should ensure that they understand how their implementation handles captured frames and any stored data.

If frames are processed locally and not saved or transmitted, the system can operate without permanently storing webcam footage.

---

#  Future Vision

The long-term goal of this project is to develop a more comprehensive **AI-powered posture assistance system** that can:

```text
Detect
   ↓
Analyze
   ↓
Classify
   ↓
Provide Feedback
   ↓
Track Improvement
```

The system could eventually provide personalized recommendations and long-term posture statistics.

---

#  Example Workflow

```text
User sits in front of webcam
              ↓
        Webcam captures frame
              ↓
        OpenCV processes frame
              ↓
      MediaPipe detects pose
              ↓
      Body landmarks extracted
              ↓
       Posture is analyzed
              ↓
       ┌───────────────┐
       │ Is posture    │
       │    correct?   │
       └───────┬───────┘
          Yes  │  No
           ↓  │   ↓
     Correct   │   Warning
     Feedback  │   Feedback
```

---

#  Dependencies

The primary dependencies used by the project include:

```text
Python
OpenCV
MediaPipe
NumPy
Hugging Face
```

For the exact versions, refer to:

```text
requirements.txt
```

---

#  Contributing

Contributions are welcome.

To contribute:

### 1. Fork the repository

```bash
git fork
```

### 2. Clone your fork

```bash
git clone <your-fork-url>
```

### 3. Create a new branch

```bash
git checkout -b feature/new-feature
```

### 4. Make your changes

Implement and test your improvements.

### 5. Commit your changes

```bash
git add .
git commit -m "Add new posture detection feature"
```

### 6. Push the branch

```bash
git push origin feature/new-feature
```

### 7. Create a Pull Request

Describe the changes and submit a pull request.

---

#  License

This project is intended for educational and development purposes.

If you plan to distribute or reuse the project, add an appropriate open-source license such as the MIT License.

---

# Author

**Riya Shukla**

B.Tech — Computer Science Engineering
Artificial Intelligence & Machine Learning

### Connect

* **GitHub:** [riya23605shukla-arch](https://github.com/riya23605shukla-arch)
* **LinkedIn:** [Riya Shukla](https://www.linkedin.com/in/riya-shukla-277495324)

---

#  Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

##  Project Summary

**Posture Correction System** is a computer-vision-based application that uses a webcam to detect human body posture in real time. By combining **Python, OpenCV, MediaPipe, and AI/ML technologies**, the system identifies posture conditions and provides immediate visual feedback.

The project demonstrates the practical application of **Artificial Intelligence, Computer Vision, Human Pose Estimation, and Real-Time Video Processing** to address an everyday problem.

# Facial Emotion Recognition Using DeepFace

## 📌 Overview

This project is a real-time **Facial Emotion Recognition** system developed using Python, OpenCV, and DeepFace.

The system captures frames from a webcam, detects human faces, analyzes facial expressions, and predicts the dominant emotion.

The project can recognize common facial emotions such as:

* Happy
* Sad
* Angry
* Fear
* Surprise
* Disgust
* Neutral

---

## 🎯 Project Goal

The main goal of this project is to explore how **facial expressions can be analyzed using computer vision and deep learning-based face analysis techniques**.

The system works in real time using a webcam and displays the detected emotion directly on the video stream.

---

## 🧠 How It Works

The system follows the pipeline below:

```text
Webcam
   ↓
Video Frame
   ↓
Face Detection
   ↓
Facial Expression Analysis
   ↓
Emotion Prediction
   ↓
Display Emotion on Screen
```

DeepFace performs the facial analysis while OpenCV handles the webcam stream and visualization.

---

## 🚀 Features

* Real-time webcam processing
* Face detection
* Facial emotion recognition
* Multiple emotion classes
* Live emotion display
* Simple Python implementation
* OpenCV-based video processing

---

## 😊 Supported Emotions

| Emotion  | Description                           |
| -------- | ------------------------------------- |
| Happy    | Positive or smiling facial expression |
| Sad      | Sad or downturned facial expression   |
| Angry    | Angry facial expression               |
| Fear     | Fearful facial expression             |
| Surprise | Surprised facial expression           |
| Disgust  | Disgusted facial expression           |
| Neutral  | No strong emotional expression        |

---

## 🛠️ Technologies

* **Python**
* **OpenCV**
* **DeepFace**

---

## 📦 Installation

Install the required Python packages:

```bash
pip install deepface opencv-python
```

---

## 📁 Project Structure

```text
facial-emotion-recognition/
│
├── emotion.py
└── README.md
```

---

## ▶️ Running the Project

Run the Python script:

```bash
python emotion.py
```

Your computer's default webcam will be opened automatically.

The predicted emotion will be displayed on the video stream.

Press:

```text
Q
```

to exit the application.

---

## 💻 Core Implementation

The webcam is initialized using OpenCV:

```python
camera = cv2.VideoCapture(0)
```

Each frame is analyzed using DeepFace:

```python
result = DeepFace.analyze(
    frame,
    actions=["emotion"],
    enforce_detection=False
)
```

The dominant emotion is then obtained:

```python
emotion = result[0]["dominant_emotion"]
```

Finally, the emotion is displayed on the video frame:

```python
cv2.putText(
    frame,
    "Emotion: " + emotion,
    (30, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)
```

---

## 📊 Example Output

The application displays the webcam feed together with the predicted emotion:

```text
Emotion: happy
```

For example:

```text
Person → Happy
```

or:

```text
Person → Neutral
```

---

## 🔬 Possible Improvements

This project can be extended in several ways.

### 1. Emotion Confidence Score

Display the probability of each emotion:

```text
Happy: 92%
Neutral: 5%
Surprise: 2%
Sad: 1%
```

### 2. Face Bounding Boxes

Draw a rectangle around every detected face and display the predicted emotion above the bounding box.

### 3. Multiple Face Recognition

Analyze multiple people in the same camera frame:

```text
Person 1 → Happy
Person 2 → Neutral
Person 3 → Sad
```

### 4. Emotion Statistics

Track the detected emotions over time and generate statistics such as:

```text
Happy    → 65%
Neutral  → 20%
Sad      → 10%
Surprise → 5%
```

### 5. Graphical User Interface

A GUI can be developed using:

* PyQt5
* Tkinter
* CustomTkinter

to create a more user-friendly application.

### 6. Video File Support

Instead of using a webcam, the system can be modified to analyze previously recorded videos.

---

## ⚠️ Limitations

Facial emotion recognition is an estimation task and should not be interpreted as a definitive measurement of a person's actual emotional state.

The prediction can be affected by:

* Lighting conditions
* Camera quality
* Face angle
* Occlusion
* Facial expressions
* Image resolution
* Multiple faces
* Individual differences in facial expressions

The system should therefore be considered an educational computer vision project rather than a reliable psychological assessment tool.

---

## 🎓 Learning Outcomes

This project provides practical experience with:

* Computer vision
* Face detection
* Facial expression analysis
* Deep learning-based face analysis
* Real-time video processing
* OpenCV
* Python
* Emotion classification

---

## 📌 Applications

Facial emotion recognition can be explored in applications such as:

* Human-computer interaction
* Educational systems
* Customer experience analysis
* Social robotics
* Smart interfaces
* Entertainment applications
* User experience research

---

## 🔮 Future Work

A more advanced version of this project could combine **face detection, emotion recognition, and temporal analysis** to understand how facial expressions change over time.

Possible future technologies include:

* CNN-based custom emotion classifiers
* Transfer learning
* LSTM-based temporal analysis
* Real-time emotion statistics
* Multi-face tracking
* PyQt5 interface
* Emotion timeline visualization

---

## 👩‍💻 Author

**Dilara Karataş**

Computer Engineering Student
Interested in Computer Vision, Artificial Intelligence and Embedded Systems.

---

## ⭐ Project Purpose

This project was developed as a practical computer vision project to explore how **facial expressions can be analyzed and classified in real time using deep learning-based tools**.


````
#  EmoTrack – Real-Time Emotion Detection using Deep Learning

EmoTrack is a real-time facial emotion detection system that uses deep learning and computer vision to classify human emotions from live webcam input.

##  Demo
> Live face detection with real-time emotion labels like Happy, Sad, Angry, etc.

---

##  Features

- Real-time webcam feed capture  
- Face detection using Haar Cascades  
- Emotion classification using a trained MobileNet-based CNN  
- Displays bounding boxes and emotion labels 


---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MaryumTanvir/real-time-face-and-emotion-detection-AI.git
cd real-time-face-and-emotion-detection-AI
````

### 2. Install Dependencies


```bash
pip install opencv-python tensorflow keras numpy matplotlib
```

### 3. Add the Trained Model

Place the trained model file in the project root directory:

* `best_model.keras` 

(You can train your own model or use a pre-trained version.)

---

##  Model Used

* **Base Architecture**: MobileNet 
* **Input Shape**: 224x224 RGB
* **Additional Layers**: GlobalAveragePooling + Dropout + Dense with Softmax
* **Dataset**: FER2013 or equivalent facial emotion dataset
* **Emotion Classes**: `angry`, `disgust`, `fear`, `happy`, `neutral`, `sad`, `surprise`

---

##  Real-World Use Cases

* Education – monitor student attention and emotions
* Mental Health – log emotional patterns during sessions
* Robotics – enhance human-machine interaction
* Gaming – adapt difficulty or narrative based on mood
* Analytics – emotion-based behavioral insights

---

## Acknowledgments

* [FER-2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013)
* [OpenCV](https://opencv.org/)
* [TensorFlow + Keras](https://www.tensorflow.org/)

```

---



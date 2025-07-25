# 🛡️ TransferOnline Proctoring System Using Data Anonymization

A secure online proctoring system that ensures exam integrity while preserving user privacy using data anonymization techniques. Designed to detect suspicious behavior and monitor candidates without exposing their personal data.

---

## 🎯 Problem Statement

Online exams face two big challenges:  
1. Preventing cheating  
2. Protecting personal data (photos, video, keystrokes)

This system handles both by integrating **data anonymization** with real-time proctoring.

---

## 🔐 Key Features

- 🧑‍💻 Real-time video surveillance via webcam
- 😶 Face anonymization using OpenCV (blur/mask techniques)
- 🧠 Behavior monitoring (gaze tracking, head movement)
- 📁 Encrypted logs of suspicious activity
- 🖥️ Admin portal for reviewing sessions
- 📡 Cloud sync + offline fallback storage

---

## 🧠 Tech Stack

| Layer        | Tech Used                          |
|--------------|-----------------------------------|
| Frontend     | HTML, CSS, JS                     |
| Backend      | Flask / Node.js (choose one used) |
| ML / CV      | OpenCV, dlib, MediaPipe           |
| Anonymization| Gaussian blur, pixel masking      |
| DB           | SQLite / MongoDB                  |

---


---

## 🧪 How It Works

1. Student logs in and starts the exam
2. Camera feed begins recording
3. Face region is anonymized (blur/pixelate)
4. Gaze/head movement is tracked for anomalies
5. Logs sent to admin dashboard

---

## 💡 Anonymization Techniques Used

- Gaussian Blur on facial regions
- Pixelation for sensitive zones
- Audio masking (optional)
- Removal of EXIF & metadata

---

## 🚀 Future Scope

- AI-based cheating pattern detection
- Blockchain-based session immutability
- Voice analysis for audio-based anomaly
- GDPR-compliant data lifecycle control

---

## ⚠️ Disclaimer

This project was created for academic purposes. Use of proctoring systems should comply with privacy laws and ethical guidelines.

---

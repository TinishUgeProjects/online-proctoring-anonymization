import cv2
import dlib
import pyaudio
import numpy as np
import pymongo
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class QuizMonitoringSystem(QMainWindow):
    def __init__(self):

        self.person_detection_count = 0
        self.last_save_time = time.time()
        super().__init__()
        self.camera = None
        self.microphone = None
        self.stream = None
        self.is_camera_on = False
        self.is_microphone_on = False
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.mongo_client["quiz_monitoring"]
        self.collection = self.db["detection_data"]
        self.lock = threading.Lock()

        self.setWindowTitle("Quiz Monitoring System")
        self.setGeometry(100, 100, 400, 200)

        self.start_button = QPushButton("Start Exam", self)
        self.start_button.setGeometry(50, 50, 200, 50)
        self.start_button.clicked.connect(self.start_exam)

        self.end_button = QPushButton("End Exam", self)
        self.end_button.setGeometry(50, 120, 200, 50)
        self.end_button.clicked.connect(self.end_exam)

        # Load YOLOv3 model
        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        self.classes = []
        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        self.multiple_person_warning_given = False
        self.no_person_warning_given = False
        self.exam_terminated = False

        self.capture_thread = threading.Thread(target=self.capture_and_save_data)
        self.capture_thread.start()

        self.face_detector = dlib.get_frontal_face_detector()
        self.landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def start_exam(self):
        self.request_permissions()

    def request_permissions(self):
        reply = QMessageBox.question(self, 'Permission Request',
                                     'Grant access to camera and microphone?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.handle_permission_granted()
        else:
            QMessageBox.information(self, 'Permission Denied',
                                    'Camera and microphone access denied.')

    def handle_permission_granted(self):
        self.start_camera()
        self.start_microphone()

        capture_thread = threading.Thread(target=self.capture_and_save_data)
        capture_thread.start()

    def start_camera(self):
        try:
            self.camera = cv2.VideoCapture(0)
            self.is_camera_on = True
        except Exception as e:
            print("Error starting camera:", e)

    def start_microphone(self):
        try:
            self.microphone = pyaudio.PyAudio()
            self.stream = self.microphone.open(format=pyaudio.paInt16,
                                               channels=1,
                                               rate=44100,
                                               input=True,
                                               frames_per_buffer=1024)
            self.is_microphone_on = True
        except Exception as e:
            print("Error starting microphone:", e)

    def end_exam(self):
        self.stop_camera()
        self.stop_microphone()
        self.exam_terminated = True

    def stop_camera(self):
        if self.camera is not None:
            self.camera.release()
            self.is_camera_on = False

    def stop_microphone(self):
        if self.microphone is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.microphone.terminate()
            self.is_microphone_on = False

    def anonymize_data(self, data):
        data_str = data.tostring()
        return hash(data_str)

    def save_to_database(self, video_data, audio_data):
        current_time = time.time()
        time_difference = current_time - self.last_save_time

        if time_difference >= 5:
            data_to_save = {
                "timestamp": current_time,
                "video_data": self.anonymize_data(video_data),
                "audio_data": self.anonymize_data(audio_data),
                "person_count": self.person_detection_count
            }
            try:
                with self.lock:
                    self.collection.insert_one(data_to_save)
            except Exception as e:
                print("Error saving to database:", e)

            self.last_save_time = current_time

    def detect_devices(self, frame):
        # Placeholder method for detecting devices (e.g., mobile phones) in the camera frame
        # You need to implement device detection logic using computer vision techniques
        # Update device_detection_count if devices are detected
        pass

    def detect_persons(self, frame):
        height, width, channels = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(output_layers)

        class_ids = []
        confidences = []
        self.device_warning_given_twice = False
        self.device_detection_count = 0
        self.person_detection_count = 0
        self.device_detection_threshold = 1
        self.person_detection_threshold = 2
        self.exam_terminated = False

        self.capture_thread = threading.Thread(target=self.capture_and_save_data)
        self.capture_thread.start()

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        self.person_detection_count = len(indexes)

    def start_exam(self):
        self.request_permissions()

    def request_permissions(self):
        reply = QMessageBox.question(self, 'Permission Request',
                                     'Grant access to camera and microphone?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.handle_permission_granted()
        else:
            QMessageBox.information(self, 'Permission Denied',
                                    'Camera and microphone access denied.')

    def handle_permission_granted(self):
        self.start_camera()
        self.start_microphone()

        capture_thread = threading.Thread(target=self.capture_and_save_data)
        capture_thread.start()

    def start_camera(self):
        try:
            self.camera = cv2.VideoCapture(0)
            self.is_camera_on = True
        except Exception as e:
            print("Error starting camera:", e)

    def start_microphone(self):
        try:
            self.microphone = pyaudio.PyAudio()
            self.stream = self.microphone.open(format=pyaudio.paInt16,
                                               channels=1,
                                               rate=44100,
                                               input=True,
                                               frames_per_buffer=1024)
            self.is_microphone_on = True
        except Exception as e:
            print("Error starting microphone:", e)

    def end_exam(self):
        self.stop_camera()
        self.stop_microphone()
        self.exam_terminated = True

    def stop_camera(self):
        if self.camera is not None:
            self.camera.release()
            self.is_camera_on = False

    def stop_microphone(self):
        if self.microphone is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.microphone.terminate()
            self.is_microphone_on = False

    def anonymize_data(self, data):
        data_str = data.tostring()
        return hash(data_str)

    def save_to_database(self, frame_data):
        current_time = time.time()
        time_difference = current_time - self.last_save_time

        if time_difference >= 5:
            data_to_save = {
                "timestamp": current_time,
                "frame_data": self.anonymize_data(frame_data),
                "person_detection_count": self.person_detection_count
            }
            try:
                with self.lock:
                    self.collection.insert_one(data_to_save)
            except Exception as e:
                print("Error saving to database:", e)

            self.last_save_time = current_time

    def detect_gaze(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector(gray)

        for face in faces:
            landmarks = self.landmark_predictor(gray, face)

            # Extract left and right eye landmarks
            left_eye_pts = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
            right_eye_pts = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

            # Detect eye movement using the positions of eye landmarks
            # Implement your eye movement detection logic here

            # Detect body movement using face landmarks or other techniques
            # Implement your body movement detection logic here

    def detect_persons(self, frame):
        height, width, channels = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.net.getUnconnectedOutLayersNames())

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and self.classes[class_id] == "person":
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        persons_detected = len(indexes)

        if persons_detected > 1:
            if not self.multiple_person_warning_given:
                QMessageBox.warning(self, 'Warning', 'Multiple persons detected.')
                self.multiple_person_warning_given = True
                self.no_person_warning_given = False  # Reset no person warning flag
            else:
                QMessageBox.critical(self, 'Exam Termination', 'Repeated multiple person detection. Exam terminated.')
                self.terminate_exam()
        elif persons_detected < 1:
            if not self.no_person_warning_given:
                QMessageBox.warning(self, 'Warning', 'No person detected.')
                self.no_person_warning_given = True
                self.multiple_person_warning_given = False  # Reset multiple person warning flag
            else:
                QMessageBox.critical(self, 'Exam Termination', 'Repeated no person detection. Exam terminated.')
                self.terminate_exam()

    def capture_and_save_data(self):
        last_save_time = time.time()  # Initialize the last save time
        while self.is_camera_on and self.is_microphone_on:
            # Capture frame from camera
            ret, frame = self.camera.read()

            # Capture audio from microphone
            audio_data = self.stream.read(1024)
            audio_array = np.frombuffer(audio_data, dtype=np.int16)

            # Calculate the time difference since the last save
            current_time = time.time()
            time_difference = current_time - last_save_time

            # Detect gaze (eye and body movements)
            self.detect_gaze(frame)

            self.save_to_database(frame)

            # Save to database if 5 seconds have elapsed since the last save
            if time_difference >= 5:
                self.save_to_database(frame, audio_array)
                last_save_time = current_time  # Update the last save time

            # Display frame (optional)
            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            time.sleep(0.1)  # Sleep for a short duration to avoid high CPU usage

        self.stop_camera()
        self.stop_microphone()
        cv2.destroyAllWindows()


    def terminate_exam(self):
        print("Exam terminated due to unauthorized activity.")
        self.end_exam()

if __name__ == "__main__":
    app = QApplication([])
    quiz_monitoring_system = QuizMonitoringSystem()
    quiz_monitoring_system.show()
    app.exec_()

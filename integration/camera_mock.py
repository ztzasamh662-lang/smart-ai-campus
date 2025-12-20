import cv2

def get_mock_camera():
    # فيديو تجريبي بدل الكاميرا
    cap = cv2.VideoCapture("test_video.mp4")
    return cap
import cv2

def get_mock_camera():
    cap = cv2.VideoCapture(0)  # webcam لو موجود
    if not cap.isOpened():
        print("No camera found, using placeholder frame")
    return cap

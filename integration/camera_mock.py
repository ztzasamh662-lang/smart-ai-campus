import cv2

def get_mock_camera():
    # فيديو تجريبي بدل الكاميرا
    cap = cv2.VideoCapture("test_video.mp4")
    return cap

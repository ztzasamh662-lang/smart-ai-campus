from camera_mock import get_mock_camera

def start_stream():
    cap = get_mock_camera()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        print("Frame received")

    cap.release()

if __name__ == "__main__":
    start_stream()
import time

def fake_camera_stream():
    """
    Simulates camera frames (no real camera)
    """
    frame_id = 0
    while True:
        frame_id += 1
        print(f"[STREAM] Sending fake frame #{frame_id}")
        time.sleep(1)

if __name__ == "__main__":
    fake_camera_stream()

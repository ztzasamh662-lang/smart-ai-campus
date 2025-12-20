from camera_mock import get_frame
import time

def send_to_ai(frame):
    print(f"[TO AI] Frame {frame['frame_id']} ready")

if __name__ == "__main__":
    for _ in range(5):
        frame = get_frame()
        print("[STREAM] Sending", frame)
        send_to_ai(frame)
        time.sleep(1)

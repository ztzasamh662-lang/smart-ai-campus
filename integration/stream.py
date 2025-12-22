from camera_mock import get_frame
from api_client import APIClient
import time

api = APIClient()

while True:
    frame = get_frame()
    print(f"[STREAM] Sending {frame}")
    api.send_frame(frame)
    time.sleep(1)

class APIClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def send_frame(self, frame):
        print(f"[API MOCK] Sending frame to {self.base_url}")
        print(frame)

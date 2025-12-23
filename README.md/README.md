# Smart AI Campus Management System

## Project Description
This project is an AI-based campus management system that handles:
- Student attendance using face recognition
- Exam monitoring and cheating detection
- Admin dashboard for monitoring and alerts

## Current Status (Week 1)
- Project structure initialized
- GitHub repository connected
- Integration module created
- Mock camera stream implemented (no real camera yet)

## Integration (Weeks 2–3)

- Implemented mock camera stream (no real camera yet)
- `camera_mock.py` generates fake frames
- `stream.py` sends frames in a loop
- `api_client.py` simulates backend API calls
- Ready to replace mock API with real backend

## Integration Module
The integration folder contains mock implementations to simulate camera input.

### Files:
- `camera_mock.py`: Simulates a camera by generating fake frames
- `stream.py`: Sends mock frames to simulate real-time streaming

> Note: This is a mock implementation. Real camera and backend APIs will be integrated later.

## How to Run
```bash
python integration/stream.py

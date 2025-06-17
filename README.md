# ATM_HELMET
ATM Security - Helmet Detection System
Overview
This project is a Streamlit-based application designed for ATM security by detecting helmets in images, videos, or live camera feeds. If a helmet is detected, the system triggers an alarm (beep sound) and simulates locking the ATM.
Features

Input Options: Upload images (JPG, JPEG, PNG), videos (MP4, AVI, MOV), or use a live camera feed (RTSP URL or device index).
Helmet Detection: Utilizes a detection service to identify helmets in the provided input.
Real-Time Feedback: Displays processed frames with detection results and alerts users via a beep sound and on-screen message when a helmet is detected.
User Interface: Built with Streamlit for an intuitive and interactive experience.

Requirements

Python 3.8+
Streamlit
OpenCV (cv2)
NumPy
Pillow (PIL)
Custom services:
DetectionService (from src.service.detection_service)
AudioService (from src.service.audio_service)



Installation

Clone the repository:git clone <repository-url>
cd <repository-directory>


Install dependencies:pip install -r requirements.txt


Ensure the DetectionService and AudioService modules are properly configured in the src/service directory.

Usage

Run the Streamlit application:streamlit run app.py


Access the web interface at http://localhost:8501.
In the sidebar, select the input type (Image, Video, or Camera).
Image: Upload an image file to process.
Video: Upload a video file to process frame-by-frame.
Camera: Provide a camera source (RTSP URL or device index, default: 0) and click "Start Camera".


If a helmet is detected, an error message appears, and a beep sound is played.

File Structure

app.py: Main Streamlit application script.
src/service/detection_service.py: Contains the DetectionService class for helmet detection.
src/service/audio_service.py: Contains the AudioService class for playing the beep sound.
requirements.txt: Lists Python dependencies.

Notes

Ensure the camera source is accessible and correctly specified for the Camera input option.
The DetectionService and AudioService classes must be implemented and configured to work with your specific model and audio setup.
Video processing creates temporary files, which are automatically deleted after use.

License
This project is licensed under the MIT License. See the LICENSE file for details.

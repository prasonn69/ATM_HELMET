import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming these are your custom modules
from src.service.detection_service import DetectionService
from src.service.audio_service import AudioService
from config import DEFAULT_CAMERA

# Initialize services
detection_service = DetectionService()
audio_service = AudioService()

# Title and Description
st.title('ATM Security - Helmet Detection System')
st.write('Upload an image or video, or use the camera to check for helmets. '
         'If a helmet is detected, the ATM will be locked or a beep sound will play.')

# Sidebar input options
input_type = st.sidebar.radio("Select Input Type", ('Image', 'Video', 'Camera'))

def process_image(image):
    """Process a single image/frame for helmet detection."""
    frame, detection_classes = detection_service.predict(image)
    if 'Helmet' in detection_classes:
        st.error("⚠️ Helmet Detected! ATM will be locked or a beep sound played.")
        audio_service.play_beep()
    return frame

def process_video(video_file):
    """Process uploaded video file."""
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    
    cap = cv2.VideoCapture(tfile.name)
    placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_image(frame)
        placeholder.image(processed_frame, channels='BGR', caption='Processing Video')

    cap.release()

def process_camera(source):
    """Process live camera feed."""
    import cv2
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        st.error("Error: Could not open camera.")
        return

    placeholder = st.empty()
    stop_button = st.button("Stop Camera")

    while True:
        ret, frame = cap.read()
        if not ret or stop_button:
            break

        processed_frame = process_image(frame)
        placeholder.image(processed_frame, channels='BGR', caption='Live Camera Feed')

    cap.release()
    st.info("Camera feed stopped.")

if input_type == 'Image':
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        processed_image = process_image(image_np)
        st.image(processed_image, caption='Processed Image', channels='BGR')

elif input_type == 'Video':
    uploaded_file = st.sidebar.file_uploader("Choose a video...", type=["mp4", "avi"])
    if uploaded_file is not None:
        process_video(uploaded_file)

elif input_type == 'Camera':
    camera_source = st.sidebar.text_input("Camera source (RTSP URL or index default:0)", str(DEFAULT_CAMERA))
    camera_source = int(camera_source) if camera_source.isdigit() else camera_source
    process_camera(camera_source)
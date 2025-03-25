import cv2
import time
import subprocess as sp
import multiprocessing as mp

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier('dataset//haarcascade_frontalface_default.xml')

# Dummy database of names (replace with your actual database)
face_names = {0: "Person 1", 1: "Person 2", 2: "Person 3"}

def process_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Loop through detected faces
    for i, (x, y, w, h) in enumerate(faces):
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Get name corresponding to the detected face (dummy example)
        name = face_names.get(i, "Unknown")
        # Write name on the frame
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return frame

def process_video():
    # Read video file
    cap = cv2.VideoCapture(file_name)

    # get height, width and frame count of the video
    width, height = (
        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter()
    out.open(output_file_name, fourcc, fps, (width, height), True)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Process frame
            frame = process_frame(frame)

            # Write the processed frame
            out.write(frame)
    except Exception as e:
        # Release resources
        print(e)
        cap.release()
        out.release()

    # Release resources
    cap.release()
    out.release()


def VideoFaceDetect() :
    print("Video processing using single process...")
    start_time = time.time()
    process_video()
    end_time = time.time()
    total_processing_time = end_time - start_time
    print("Time taken: {}".format(total_processing_time))
    print("Video frame count = {}".format(frame_count))
    print("FPS : {}".format(frame_count/total_processing_time))


def get_video_details(file_name):
    cap = cv2.VideoCapture(file_name)
    length = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FRAME_COUNT))
    width = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cv2.VideoCapture.get(cap, cv2.CAP_PROP_FRAME_HEIGHT))
    return [width, height, length]


fn = "test_Trim"
file_name = fn+".mp4"
output_file_name = fn+"_output_single.mp4"
width, height, frame_count = get_video_details(file_name)
print("Video frame count = {}".format(frame_count))
print("Width = {}, Height = {}".format(width, height))
VideoFaceDetect()
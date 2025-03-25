import cv2
import time

def ImageFaceDetect(fn, filename):
    start_time = time.time()
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('dataset//haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread(filename)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    end_time = time.time()
    print(fn, "single time:", (end_time-start_time))
    print("Number of faces detected:", len(faces))

    # Calculate accuracy (assuming we have ground truth)
    # Replace this with actual ground truth if available
    ground_truth = 100  # For example, 1 face in the image
    detected_faces = len(faces)
    accuracy = (detected_faces / ground_truth) * 100
    if accuracy > 100:
        accuracy = 100 - (accuracy - 100)  # Subtract the difference from 100
    print("Accuracy:", accuracy, "%")

    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()  # Close all windows after key press
    del face_cascade
    del img
    del gray
    del faces

if __name__ == '__main__':
    fn = "test2"
    file_name = fn + ".jpeg"
    ImageFaceDetect(fn, file_name)

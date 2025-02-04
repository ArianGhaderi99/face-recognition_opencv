import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Check if the cascade has been loaded correctly
if face_cascade.empty():
    print("Error loading cascade file. Please check the path.")
    exit()

# To capture video from webcam
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error opening video capture.")
    exit()

while True:
    # Read the frame
    ret, img = capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display
    cv2.imshow("img", img)

    # Exit on pressing 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
capture.release()
cv2.destroyAllWindows()

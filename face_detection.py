import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)
if not vid.isOpened():
    raise RuntimeError("Cannot open webcam")

# Video writer
output = cv2.VideoWriter(
    "face_detection.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    20,
    (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))))

try:
    while True:
        ret, frame = vid.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)
        output.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    vid.release()
    output.release()
    cv2.destroyAllWindows()
from deepface import DeepFace
import cv2

# Kamerayı aç
camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        emotion = result[0]["dominant_emotion"]

        cv2.putText(
            frame,
            "Emotion: " + emotion,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    except:
        pass

    cv2.imshow("Emotion Recognition", frame)

    # Q ile çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
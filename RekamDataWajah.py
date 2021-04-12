import cv2

cam = cv2.VideoCapture(2)
cam.set(3, 648)
cam.set(4, 488)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier('haarcascade_eye.xml')
faceID = input("Masukan Face ID  yang akan Direkam Datanya: ")
print("Tatap wajah anda ke depan anda ke dalam webcam")
while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3,
                                          5)  #frame, scaleFactor, minNeoghnour
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roiAbuabu = abuAbu[y:y + h, x:x + w]
        roiWarna = frame[y:y + h, x:x + w]
        eyes = eyeDetector.detectMultiScale(roiAbuabu)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roiWarna, (xe, ye), (xe + we, ye + he), (0, 0, 255),
                          1)
    cv2.imshow('Webcamku', frame)
    #cv2.imshow('Webcameku 2 ', abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break
cam.release()
cv2.destroyAllWindows()
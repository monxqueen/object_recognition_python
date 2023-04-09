import cv2

video = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('cascade_caneca3.xml')

while True:
    conectado, frame = video.read()

    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    deteccoes = classificador.detectMultiScale(imagemCinza)
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(frame, (x,y), (x+l, y+a), (0,0,255), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
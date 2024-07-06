import cv2
import winsound

cam = cv2.VideoCapture(0)

while True:
    _, frame1 = cam.read()
    _, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    frame = cv2.flip(diff, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_frame, 20, 255, cv2.THRESH_BINARY)
    cont, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for i in cont:
        if cv2.contourArea(i) < 5000 :
            continue
        winsound.Beep(5000, 500)
    
    cv2.imshow('Motion Detecting Window', thresh)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
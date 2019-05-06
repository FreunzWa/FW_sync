import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#take the video's first frame
ret, frame = cap.read()

while True:
	#take the video's frame for each cycle
	ret, frame = cap.read()

	cv2.imshow('Output Video', frame)

    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()
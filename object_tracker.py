from centroidtracker import CentroidTracker
from imutils.video import VideoStream
import numpy as np
import argparse, imutils, time, cv2, csv, re, sys, traceback
import pandas as pd 

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

ct = CentroidTracker()
(H, W) = (None, None)

net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
vs = cv2.VideoCapture(args["video"])

fields=['study','video','performance']
fields1=[args["video"][-5:6],args["video"][:6],'performance']
with open('data.csv','a', newline='') as f:	
	writer = csv.writer(f)
	writer.writerow(fields)
	writer.writerow(fields1)

while True:
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	frame = imutils.resize(frame, width=1800)
	(H, W) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H),
		(104.0, 177.0, 123.0))
	net.setInput(blob)
	detections = net.forward()
	rects = []

	for i in range(0, detections.shape[2]):
		if detections[0, 0, i, 2] > args["confidence"]:
			box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
			rects.append(box.astype("int"))
			(startX, startY, endX, endY) = box.astype("int")
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 255, 0), 2)

	objects = ct.update(rects)
	
	file=open( "data.csv", "r")
	reader = csv.reader(file)
	lines = list(reader)
	lines[1][2] = str(list(objects.keys())[-1]+1)
	with open('data.csv', "w") as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(lines) 

	for (objectID, centroid) in objects.items():
		text = "Person {}".format(objectID+1)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cv2.destroyAllWindows()
sys.exit(1)


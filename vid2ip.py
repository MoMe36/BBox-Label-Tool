import cv2
import numpy as np 
from argparse import ArgumentParser 
from PIL import Image 

parser = ArgumentParser()

parser.add_argument('--in_path', default ="/home/mehdi/Images/1.mp4")
parser.add_argument('--out_path', default ="./dataset/")
parser.add_argument('--save_every', type = int, default = 250)
args =parser.parse_args()


def nb_frames(cap): 
	return (cap.get(cv2.CAP_PROP_FRAME_COUNT))


cap = cv2.VideoCapture(args.in_path)

max_frames = nb_frames(cap)
current_frame = 0 

saved = 0
while cap.isOpened(): 

	

	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	if(current_frame % args.save_every) == 0:

		current_image = Image.fromarray(frame)
		current_image.save('{}{}.jpg'.format(args.out_path, saved))
		cv2.imwrite('{}{}.jpg'.format(args.out_path, saved), frame)
		saved += 1

		print('Frames: {}/{} \t Saved: {}'.format(current_frame, int(max_frames), saved))

	if saved > 25: 
		break 


	current_frame += 1

cap.release()


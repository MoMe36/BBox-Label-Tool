import csv 
import os 
import glob



class_dict = {}
with open('class.txt', 'r') as class_text: 
	class_it = 0
	for l in class_text:
		if l != "": 
			if l.endswith('\n'): 
				l = l[:-1]
			class_dict[l] = class_it
			class_it += 1

def parse_label_file(path):
	
	with open(path, 'r') as l_file: 
		next(l_file)
		data = []
		for l in l_file:
			if l.endswith('\n'): l = l[:-1] 

			f_l = l.split(' ')

			f_l[-1] = class_dict[f_l[-1]]
			f_l = [int(f_) for f_ in f_l]
			data.append(f_l)

	return data

labels_path = './Labels/'
image_path = '/home/mehdi/Codes/ObjectDetection/melo_dataset/'


files = glob.glob(labels_path + "*.txt") 
nb_files = len(files)


with open(labels_path + 'train.txt', 'w') as file: 

	for i in range(nb_files-1): 
		current_data = parse_label_file('{}{}.txt'.format(labels_path, i))

		point = image_path + '{}.jpg'.format(i) + ' '
		for box_counter, box in enumerate(current_data): 
			for j,p in enumerate(box): 
				point += str(p)
				if(j < len(box) -1 ): point += ","

			if box_counter < (len(box)-1): 
				point += ' '

		if point.endswith(' '): 
			point = point[:-1]
		file.write(point + '\n') 
		# writeline(current_data)
import cv2 as cv
import time
import numpy as np
import imutils
import functools
import simpleaudio
import string
from tkinter import *
from tkinter.ttk import *

import testTypes

#print(cv.__version__)


cap = cv.VideoCapture(0)

while not cap.isOpened():
	time.sleep(.5)
	cap = cv.VideoCapture(0)

ret, src = cap.read()

print("Camera open")
w, h = src.shape[1::-1]

########### COLOR MASKS ###########
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
###################################



global roi_x_axis, roi_y_axis

config_file = open('config.txt', 'rt')
positional_data_raw = config_file.read()
config_file.close()

positional_data = positional_data_raw.split(',')

roi_x_axis = int(positional_data[0])
roi_y_axis = int(positional_data[1])

def assingNewXAxisValue(X):
	global roi_x_axis
	roi_x_axis = X

def assingNewYAxisValue(Y):
	global roi_y_axis
	roi_y_axis = Y

SCALE_PERCENT = 50
WIDTH = int(w  * SCALE_PERCENT/100)
HEIGHT = int(h  * SCALE_PERCENT/100)

newDimensions = (WIDTH, HEIGHT)

sectionHeight = (100,380)
section1 = (400, 590)
section2 = (210,400)
section3 = (20,210)
visual_sugar = -5

sectionGroup = [section1, section2, section3]

def play_sound(ok):
  
	if ok == 'FAILED':
		wave_obj = simpleaudio.WaveObject.from_wave_file("bad.wav")
	elif ok == 'PASS':
		wave_obj = simpleaudio.WaveObject.from_wave_file("ToneUp.wav")
	play_obj = wave_obj.play()
##	play_obj.wait_done() Waits for audio to finish


def pointInRect(point, rect):
	x1, y1, x2, y2 = rect
	x, y = point
	if (x1 < x and x < x2):
		if (y1 < y and y < y2):
			return True
	return False


def generateMsk(hsv, colors):
	msk = cv.inRange(hsv, colors[0], colors[1])
	return msk


def generateROI(img, positions, positionsCheck):
	#for position in positions:
	global roi_x_axis, roi_y_axis
	print("GENERATE ROI")
	print(positions)
	print(positionsCheck)
	for i in range(0, len(positions)):
		position = positions[i]
		roi_color = (255, 0, 0)
		isFail = False

		if len(positionsCheck) > 0:
			if positionsCheck[i] == 1:
				roi_color = (0, 200, 0)

			if positionsCheck[i] == -1:
				roi_color = (0, 0, 255)
				isFail = True

			if positionsCheck[i] == 0:
				roi_color = (255, 0, 0)

		position_1 = (position[0][0] + roi_x_axis, position[0][1] + roi_y_axis)
		position_2 = (position[1][0] + roi_x_axis, position[1][1] + roi_y_axis)
		img = cv.rectangle(img, position_1, position_2, roi_color, FIGURES_THICKNESS, cv.LINE_4)
		print(isFail)
		if isFail:
			img = cv.putText(img, 'Error', (position_2[0] + 5, position_2[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, roi_color, FIGURES_THICKNESS)
	
	return img

def assertPartNumber(window, testType, message):
	global sectionPositionsGroup
	global isPartNumber
	global messageState

	sectionPositionsGroup = testType
	isPartNumber = True
	messageState = message
	window.destroy()





def getBarcode(window, text):
	global sectionPositionsGroup
	global isPartNumber
	global isTest
	key = text
	print(f'repr: {repr(key)}')
	key = key.replace("'", "")
	print(key)

	key_header = key[0:3]
	if key_header == "003":
		if key == "0033105010":
			assertPartNumber(window, testTypes.test_003_31050_10, "ID/Numero de parte")

		if key == "0033104910":
			assertPartNumber(window, testTypes.test_003_31049_10, "ID/Numero de parte")

		if key == "0033104900":
			assertPartNumber(window, testTypes.test_003_31049_00, "ID/Numero de parte")

		if key == "0033104810":
			assertPartNumber(window, testTypes.test_003_31048_10, "ID/Numero de parte")

		if key == "0033046610":
			assertPartNumber(window, testTypes.test_003_30466_10, "ID/Numero de parte")

		if not isPartNumber:
			window.destroy()
	else:
		print( sectionPositionsGroup is not None )
		if sectionPositionsGroup is not None:
			isTest = True
			window.destroy()
		else:
			window.destroy()


#The positions of the ROIS
global sectionPositionsGroup 
sectionPositionsGroup = None

# Flag to check if the received parameter its actually a valid barcode
global isTest 
isTest = False

# Flag to check if a part number exist
global isPartNumber
isPartNumber = False

# Counter to move between detection sections
sectionCounter = 0

# Flag used to mark failed sections on green
isError = False

# State for the scanning message
messageState = "numero de parte"

while True:
	
	while True:
		# ret, src = cap.read()
		master = Tk()
		master.title("Codigo de barras")
		master.geometry("500x100")
		
		label = Label(master,text =f"Escanee el {messageState}")
		label.pack(pady = 10)
		label.config(font=('Helvetica bold', 25))

		entry= Entry(master, width= 40)
		entry.focus_set()
		entry.bind('<Return>', lambda a: getBarcode(master, entry.get()))
		entry.pack()

		master.mainloop()

		if isTest:
			break


	FIGURES_THICKNESS = 2

	# Count the iterated sections, starts at the minimun position depending of the quantity of section of the pcb
	sectionCounter = 3 - (len(sectionPositionsGroup))

	# Counts the actual quantity of inspection zones on the pcb
	roi_logical_section = 0
	
	sectionsPassed = 0
	sections_passed = []
	ROI_passed_check = []
	last_section = 'n'

	while True:
		cv.namedWindow('Configurations')
		cv.createTrackbar('X axis', 'Configurations', roi_x_axis, 200, assingNewXAxisValue)
		cv.setTrackbarMin('X axis', 'Configurations', -200)
		cv.setTrackbarPos('X axis', 'Configurations', roi_x_axis)
		cv.createTrackbar('Y axis', 'Configurations', roi_y_axis, 200, assingNewYAxisValue)
		cv.setTrackbarMin('Y axis', 'Configurations', -200)
		cv.setTrackbarPos('Y axis', 'Configurations', roi_y_axis)

		while True:
			ret, src = cap.read()

			sectionValues = sectionGroup[sectionCounter]

			side_color = (255, 0, 0)
				
			sideImage = cv.resize(src.copy(), newDimensions)

			for section in sections_passed:
				section_passed = sectionGroup[section]
				sideImage = cv.putText(sideImage, 'PASS', (int(section_passed[0]/2) + 10, 120), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), FIGURES_THICKNESS)
				sideImage = cv.rectangle(sideImage, (int(section_passed[1]/2),20), (int((section_passed[0] - visual_sugar)/2),200), (0, 200, 0), FIGURES_THICKNESS, cv.LINE_4)


			if isError:
				side_color = (0, 0, 255)
				# (sectionValues[1], sectionHeight[1]/2)
				sideImage = cv.putText(sideImage, 'FAIL', (int(sectionValues[0]/2) + 18, 120), cv.FONT_HERSHEY_SIMPLEX, 1, side_color, FIGURES_THICKNESS)

			sideImage = cv.rectangle(sideImage, (int(sectionValues[1] /2),20), (int((sectionValues[0] - visual_sugar)/2),200), side_color, FIGURES_THICKNESS, cv.LINE_4)
			cv.imshow('Preview', sideImage)

			sectionImg = src[sectionHeight[0]:sectionHeight[1], sectionValues[0]:sectionValues[1]]
			
			roi_set = sectionPositionsGroup[roi_logical_section]
			if last_section != roi_logical_section:
				ROI_passed_check = [0 for roi in roi_set]
			
			sectionImgRoi = generateROI(sectionImg.copy(), roi_set, ROI_passed_check)
			cv.imshow('Navico', sectionImgRoi)
			
			key = cv.waitKey(2)
			        
			
			if key is ord('b'):
				break
		
		#####################################################################
		config_file = open('config.txt', 'wt')
		config_file.write(f'{roi_x_axis},{roi_y_axis}')
		config_file.close()

		cv.putText(sectionImgRoi, 'PROBANDO...',(10,15),cv.FONT_HERSHEY_SIMPLEX, 0.6, [250,0,0], 1)
		cv.imshow('Navico',sectionImgRoi)
		
		
		roiPositions = sectionPositionsGroup[roi_logical_section]
		roiPLength = len(roiPositions)
		ROI_passed_check = [0 for roi in roiPositions] # Fill the array with zeros, to replace them with one if a roi fails

		
		################## color hold flags for welding boxes ######################
		failClassArray = np.zeros(roiPLength, dtype=int)
		print(f'fail array: {failClassArray}')

		passClassArray = np.zeros(roiPLength, dtype=int)
		print(f'pass array: {passClassArray}')

		print(f'Size roiP: {len(roiPositions)}')
		for i in range(0, roiPLength):

			clas = i
			print('CLASS',clas)
			
			TRH = 3
			NL_TRH = 15

			k1 = 0
			NL = 0

			roi_point1_recalculated = (roiPositions[i][0][0]  + roi_x_axis, roiPositions[i][0][1]  + roi_y_axis)
			roi_point2_recalculated = (roiPositions[i][1][0]  + roi_x_axis, roiPositions[i][1][1]  + roi_y_axis)

			roi = (roi_point1_recalculated, roi_point2_recalculated)
			print(roi)
			print('^^^^^^')
			roi_pt1 = roi[0]
			roi_pt2 = roi[1]
			WEL_BOXA_PT1 = roi_pt1
			WEL_BOXA_PT2 = roi_pt2
		
			while True:
					
				src1 = sectionImg.copy()
				

				img_crop = src1[roi_pt1[1]:roi_pt2[1], roi_pt1[0]:roi_pt2[0]]
				redSquare = cv.rectangle(src1.copy(), roi_pt1,roi_pt2,(0,0,255), FIGURES_THICKNESS, cv.LINE_4)
				cv.imshow('Navico', redSquare)
				cv.waitKey(3)
				src = img_crop
		
				#####################################  MASKING START   ################################
				print(f'Valor de i: {i}')
				hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
				msk1 = generateMsk(hsv,roiPositions[i][2])


				kernelmatrix = np.ones((2,2), np.uint8)
				msk_DIL = cv.dilate(msk1, kernelmatrix)
	#             cv.waitKey(300)
				
				linesP = cv.HoughLinesP(msk_DIL, 1, np.pi / 45, 10, 65, 10, 2)
				
					

				if linesP is None:
					if NL == NL_TRH:
						print('NO LINE DETECTED in Class ',clas,NL)
						ROI_passed_check[i] = -1
						break
					else:
						NL = NL + 1
						ROI_passed_check[i] = -1
					
				elif linesP is not None:
		
					for j in range(0, len(linesP)):
						l = linesP[j][0]
						cv.line(img_crop, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

						rotated = imutils.rotate(src1, 0)                   
						cv.imshow('Navico', rotated)
						cv.waitKey(150)
						
						Result_Point = ( l[0], l[1])

						##########   PRINTS OUT SMAL BLUE RECTANGLE TO SHIW WIRE POSITION VS WELDING BOX ##########
						img_rect = cv.rectangle(src1, roi_pt1,roi_pt2,(0,255,0), FIGURES_THICKNESS, cv.LINE_4)

						Result_Point1 = (roi[0][0]+l[0],roi[1][1]+l[1])
						Result_Point2 = (roi[0][0]+l[2],roi[1][1]+l[3])

						########## CHECKS IF THE BLUE DOT IS IN RANGE OF A WLDING BOX AND COUNTS IT IN THAT BOX ##########
						if pointInRect(Result_Point1, ( WEL_BOXA_PT1[0], WEL_BOXA_PT1[1], WEL_BOXA_PT2[0], WEL_BOXA_PT2[1] ) ):
							k1 = k1 + 1
							ROI_passed_check[i] = 1

						elif pointInRect(Result_Point2, ( WEL_BOXA_PT1[0], WEL_BOXA_PT1[1], WEL_BOXA_PT2[0]+50, WEL_BOXA_PT2[1]+50 ) ):
							k1 = k1 + 1
							ROI_passed_check[i] = 1

						else:
							NL = NL + 1
							ROI_passed_check[i] = -1
				
				print(f'NL: {NL}')
				print(f'K1: {k1}')
				
				if NL >= NL_TRH:
					failClassArray[clas] = 1
					print('class',clas, 'NL=',NL,'K=', k1)
					break
				
				elif k1>=TRH:
					passClassArray[clas] = 1
					print('class',clas, 'NL=',NL,'K=', k1)          
					break

		print(f'Values fail: {failClassArray}')
		print(f'Values pass: {passClassArray}')
		
		print(f'ROI passed: {ROI_passed_check}')
		last_section = roi_logical_section

		if  functools.reduce(lambda a, b: a+b, passClassArray) >= roiPLength: #  or True
			ROI_BOX_CLR = (0,255,0)
			ROI_BOX_CLR1 = (0,255,0)
			ROI_BOX_CLR2 = (0,255,0)
			ROI_BOX_CLR3 = (0,255,0)
			ROI_BOX_CLR4 = (0,255,0)
			WEL_BOXA_CLR = (0,255,0)
			WEL_BOXB_CLR = (0,255,0)
			validPart = True
			isError = False
			print('PASS')

			sections_passed.append(sectionCounter)
			sectionsPassed = sectionsPassed + 1
			sectionCounter = sectionCounter + 1
			roi_logical_section = roi_logical_section + 1 

			if sectionCounter > 2:
				sectionCounter = 0

			if roi_logical_section > len(sectionPositionsGroup):
				roi_logical_section = 0
			
			play_sound('PASS')

		else:
			play_sound('FAILED')
			print('FAILED')
			isError = True

		# Redraw ROI
		key = cv.waitKey(1)       
		
		if( sectionsPassed == len(sectionPositionsGroup)):
			cv.destroyWindow('Navico')
			cv.destroyWindow('Configurations')
			for section in sections_passed:
				section_passed = sectionGroup[section]
				sideImage = cv.putText(sideImage, 'PASS', (int(section_passed[0]/2) + 10, 120), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), FIGURES_THICKNESS)
				sideImage = cv.rectangle(sideImage, (int(section_passed[1]/2),20), (int((section_passed[0] - visual_sugar)/2),200), (0, 200, 0), FIGURES_THICKNESS, cv.LINE_4)
			cv.imshow('Preview', sideImage)
			cv.waitKey(1)
			break
		############# LOOP END ##############

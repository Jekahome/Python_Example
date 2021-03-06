#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2 
'''
    захват видео
'''

cv2.namedWindow("preview") 
vc = cv2.VideoCapture(0) 

if vc.isOpened(): # try to get the first frame 
    rval, frame = vc.read() 
else: 
    rval = False 

while rval: 
    cv2.imshow("preview", frame) 
    rval, frame = vc.read() 
    key = cv2.waitKey(1) # 1 ms delay
    if key == 'q' or key == 27: # exit on ESC break 
        cv2.destroyWindow("preview")

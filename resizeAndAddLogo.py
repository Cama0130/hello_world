#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resizeAndAddLogo.py - resize imgfile to "300x300" size and add logo file to the lower-right corner.
Created on Thu Aug 19 16:02:23 2021

@author: hee-bumyang
"""
import sys, os
from PIL import Image

#1-1. define in_file and out_file directory and logofile path
os.makedirs('in_file', exist_ok=True)
os.makedirs('out_file', exist_ok=True)
inDirect = 'in_file'
outDirect = 'out_file'
logoName = 'resizedCat.png'

#1-2. define resized size and make image object for logofile
resizingScale = 300
logoImg = Image.open(logoName)
(logoWidth, logoHeight) = logoImg.size

#2-1. make a list of file in in_file
fileList = os.listdir('in_file')

#2-2. load each image file for the resizing and adding logo
for file in fileList :
    #2-2-1. exclude non-image type file
    if not (file.endswith('.png') or file.endswith('.jpg')) :
        continue
    #2-2-2. load image file and calculate resizing width and height
    img = Image.open(file)
    imgWidth, imgHeight = img.size
    if imgWidth > imgHeight :
        Width = resizingScale
        Height = int(imgHeight*(resizingScale/imgWidth))
    else :
        Height = resizingScale
        Width = int(imgWidth*(resizingScale/imgHeight))

    print('Resizing image file of %s' % file)    
    #2-2-3. resize image file
    resizedImg = img.resize((Width, Height))
    #2-2-4. add logo to resized image file
    resizedImg.paste(logoImg, (Width-logoWidth, Height-logoHeight), logoImg)
    #2-2-5. save file
    fileNameEle = file.split('.')
    newFile = fileNameEle[0] + '_add_logo.' + fileNameEle[1]
    resizedImg.save(os.path.join(outDirect, newFile))
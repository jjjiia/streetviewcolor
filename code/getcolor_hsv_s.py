from __future__ import with_statement

import os
import os.path
import Image
import math
import csv
import sys
#FUNCTION FOR CONVERTING RGB TO HSV
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h,s,v

#MAKE LIST OF FILES IN A DIRECTORY
for path, subirs, files in os.walk(r'/Users/jiazhang/Documents/GitHub/streetviewcolor/NewYork_40.736516_-74.0075864066_40.7628541651_-73.9656092319'):
    currentdir = []
    files = [f for f in files if not f[0] == '.']
    for filename in files:
        #JOIN NAME WITH PATH
        f = os.path.join(path, filename)
        currentdir.append(f)       
   # print currentdir
values = []
#MAKE DICTIONARY
valuefreq={}
allh =[]

#OPEN FILES IN LIST AND GET COLOR
basepath = '/Users/jiazhang/Documents/GitHub/streetviewcolor/'
with open(basepath+'Sat_40.736516_-74.0075864066_40.7628541651_-73.9656092319.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    print "open"
    for file in currentdir:
        #print file
        group1 = 0
        group2 = 0
        group3 = 0
        group4 = 0
        group5 = 0
        group6 = 0
        group0  = 0
        image = Image.open(file)
        width, height = image.size
        imgstat = os.stat(file)
        pix = image.load()
        #print imgstat
        #print imgstat[6]
        #CHECK IF IMAGE IS BLANK, AND REMOVE
        if imgstat[6] < 4483:
            os.remove(file)
        for x in range(0,width):
            for y in range(0,height):
                r,g,b = pix[x,y]
                rgb = (r,g,b)
                hexcode = '#'+''.join(map(chr, rgb)).encode('hex')
                #print hexcode
                h,s,v = rgb2hsv(r,g,b)
                hgroup = int(s*100/20)
                if hgroup == 1:
                    group1 = group1+1
                if hgroup == 2:
                    group2 = group2+1
                if hgroup == 3:
                    group3 = group3+1
                if hgroup == 4 or hgroup == 5 :
                    group4 = group4+1
                if hgroup ==0:
                    group0 = group0+1
                
        latlng = str(file).split("_")
        lat = latlng[-3].split("/")[-1]
        lng = latlng[-2]
        
       # print lat, lng
        total = group1+group2+group3+group4+group0
        imagedata = [group0, group1,group2,group3,group4, total, lat, lng]
        print imagedata
        spamwriter.writerow(imagedata)
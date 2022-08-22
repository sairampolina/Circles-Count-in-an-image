
"""
Created on Tue Mar 15 19:30:07 2022

Brief: Code to count the no of white blobs in an image .

@author: Sairam Polina
"""

import cv2
import numpy as np

# reading the image
image=cv2.imread('../Data/connectedcircles.png')


# converting to gray scale
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# converting to binary
ret,bin_image=cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('binary image',bin_image)
# cv2.imwrite('../Results/binaryImage.png',bin_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# creating structural element as kernel  
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (51,51))

# performing opening operation
opened_image=cv2.morphologyEx(bin_image, cv2.MORPH_OPEN, kernel)

cv2.imshow('Image after opening',opened_image)
# cv2.imwrite('../Results/imageAfterOpening.png',opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# =============================================================================
#  counting number of circles with cv2.HoughCircles()
# =============================================================================

# finding number of circles in opened_image
circles = cv2.HoughCircles(opened_image,cv2.HOUGH_GRADIENT,1.2,25,param1=30,param2=25,minRadius=0,maxRadius=35)

#gray image to BGR image
displayImage=cv2.cvtColor(opened_image, cv2.COLOR_GRAY2BGR)

disIm=displayImage.copy()

# drawing circles on to  the image
for circle in circles[0]:
    
    centerX=int(circle[0])
    centerY=int(circle[1])
    r=int(circle[2])
    cv2.circle(disIm,(centerX,centerY),r,(0,255,0),2)
    cv2.circle(disIm,(centerX,centerY),2,(0,0,255),5)

cv2.imshow('circles detected by cv2.HoughCircles',disIm)
# cv2.imwrite('../Results/CirclesDetected_with_HoughCircle.png',disIm)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Number of circles detected  by Hough Circles:',len(circles[0]))
 


# =============================================================================
# option2-Count of circles through CCA(Connected Component Analysis)
# =============================================================================

ret,im_labels=cv2.connectedComponents(opened_image)

print(f"Number of circles detected by Connected Compont Analysis: {im_labels.max()}")

#visulazing CCA image

minVal=im_labels.min()
maxVal=im_labels.max()

# normalizing pixel values in between 0 and 255
normalized_image=255*(im_labels-minVal)/(maxVal-minVal)

normalized_image=np.uint8(normalized_image)
# gray_normalized_image=
colormapped_image=cv2.applyColorMap(normalized_image,cv2.COLORMAP_JET)

cv2.imshow('CCA image after colormapping', colormapped_image)
# cv2.imwrite('../Results/CirclesDetected_with_CCA.png',colormapped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# =============================================================================
# option3-counting no of circles with findContours()
# =============================================================================

contours,hierarchy=cv2.findContours(opened_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Number of circles detected by find Contours: {len(contours)}")

#drawing countours obtained
cv2.drawContours(displayImage, contours, -1, (0,0,255),2)

#displaying and saving image
cv2.imshow('Circles detected by find Contours',displayImage )
# cv2.imwrite('../Results/CirclesDetected_with_findContours.png',displayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

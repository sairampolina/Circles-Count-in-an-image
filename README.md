# Count of circles in an image

## Original Image
![connectedcircles](https://user-images.githubusercontent.com/48856345/185826827-b83bf6dc-ece0-424d-b1ff-3cc03ef219c1.png)

##  Image after Binary Thresholding
![binaryImage](https://user-images.githubusercontent.com/48856345/185826835-ff28bdef-1f68-4b4f-98ce-cedd9a6aaf66.png)

## Image after Morphological Opening with Ellipse Kernel
![imageAfterOpening](https://user-images.githubusercontent.com/48856345/185826847-5afbd341-875b-4424-bc4b-5f2b23d78469.png)


## Circles Detected by cv2.HoughCircles()
![CirclesDetected_with_HoughCircle](https://user-images.githubusercontent.com/48856345/185827281-c1aab5e8-fb76-4bbc-bcdf-8d6752f010a5.png)

## Circles Detected by cv2.connectedComponents()

![CirclesDetected_with_CCA](https://user-images.githubusercontent.com/48856345/185827289-2453d967-e944-40c5-ba5a-c3bbaf17ed3e.png)


## Circles Detected by cv2.findContours()
![CirclesDetected_with_findContours](https://user-images.githubusercontent.com/48856345/185827298-dfb6edea-27d8-44a7-adc2-c420dc07f656.png)

## In each of the above cases all circles were detected and dimensions of returned values of this functions can be used to determine "Number of Circles."

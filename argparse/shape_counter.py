import argparse
import cv2
import imutils

AP = argparse.ArgumentParser()
AP.add_argument("-i", "--input", required=True, help="path to input image")
AP.add_argument("-o", "--output", required=True, help="path to output image")
ARGS = vars(AP.parse_args())

image = cv2.imread(ARGS["input"])

# convert the image to GRAYscale, blur it, and threshold it
GRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(GRAY, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cnts= cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts= imutils.grab_contours(cnts)

for c in cnts:
    cv2.drawContours(image, [c], -1, (0, 0, 255), 2)

text = "I found {} total shApes".format(len(cnts))
cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
# write the output image to disk
cv2.imwrite(ARGS["output"], image)

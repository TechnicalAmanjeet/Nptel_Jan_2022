# in this segment will show how we can enhance our image

import cv2 as cv

# read image by using cv2 in program
img = cv.imread("aman_img.jpg")  # read color in the form form of bgr.
# print(img)

# will applay clahe concept here
# create object for clahe
clahe = cv.createCLAHE()  # initialized clahe object.

# since clahe work on gray color img.
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converted img into gray format
cv.imwrite("gray_color.png", gray_img)  # cmd to save img in the local storage.

# apply enhancement by using clahe concept
enhance_img = clahe.apply(gray_img)

# save enhance_img into local storage.
cv.imwrite("enhanced_img.png", enhance_img)

print("done with enhancement of img")


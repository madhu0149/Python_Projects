import cv2

path = input("Enter the path to the photo you want to resize :\n")
dest = input("Enter the destination to store the resized photo :\n")
src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src)

scale_percent = int(input('Enter the scaling percentage :\n'))

width = int(src.shape[1]*scale_percent/100)
length = int(src.shape[1]*scale_percent/100)

dsize = (width, length)

output = cv2.resize(src, dsize)

cv2.imwrite(dest, output)
cv2.waitKey(0)
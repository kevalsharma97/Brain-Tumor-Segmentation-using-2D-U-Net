import shutil
import cv2
import os
import win32api

image_slice_path = r"D:\Segmentation\Brain_Images\train\slices/" # Path to images
image_slice_path = win32api.GetShortPathName(image_slice_path)
moveto = r"D:\Segmentation\Brain_Images\train\black/"   # Path to store blank images
moveto = win32api.GetShortPathName(moveto)
label_slice_path = r"D:/Segmentation/Brain_Images/labels/slices/"   # Path to labels
label_slice_path = win32api.GetShortPathName(label_slice_path)
moveto_new = r"D:/Segmentation/Brain_Images/labels/black/"  # Path to store blank labels
moveto_new = win32api.GetShortPathName(moveto_new)

count = 0
ctr = 0
for file in os.listdir(image_slice_path):
    img = cv2.imread(os.path.join(image_slice_path, file))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    x, y = os.path.split(image_slice_path + file)
    a, b = os.path.splitext(y)
    print("Checking " + str(y))
    if cv2.countNonZero(blackAndWhiteImage) == 0:
        print("Moving " + str(a) + " file")
        src = image_slice_path + file
        dest = moveto + file
        shutil.move(src, dest)

        src_new = label_slice_path + file
        dest_new = moveto_new + file
        shutil.move(src_new, dest_new)
        # print("Image " + str(a) + " is black")
        ctr = ctr + 1
    # else:
    #     print("Image " + str(a) + " is fine")
print(ctr)
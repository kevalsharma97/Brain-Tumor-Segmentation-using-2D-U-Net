import cv2
import os

image_slice_path = r"D:/Segmentation/Brain_Images/train/slices/"    # Path to image slices
label_slice_path = r"D:/Segmentation/Brain_Images/labels/slices/"   # Path to image labels

for file in os.listdir(image_slice_path):
    img = cv2.imread(os.path.join(image_slice_path, file))
    x, y = os.path.split(image_slice_path + file)
    # print(img.shape)
    dim = (155, 240)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    os.chdir(image_slice_path)
    # print(resized.shape)
    cv2.imwrite(str(y), resized)
    print("File " + str(y) + " resized")
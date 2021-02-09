import nibabel as nib
import os
from nilearn import plotting, image, datasets

# Path to training images
imagePath = "D:/Study/Sem-4/Project/Image Segmentation/Dataset/Task08_HepaticVessel/imagesTr/"

# Path to store the training images converted to png
trainPath = "D:/Study/Sem-4/Project/Image Segmentation/Dataset/Task08_HepaticVessel/PNG files/train/"

# Path to store the labels converted to png
labelsPath = "D:/Study/Sem-4/Project/Image Segmentation/Dataset/Task08_HepaticVessel/PNG files/labels/"
testPath = "D:/Study/Sem-4/Project/Image Segmentation/Dataset/Task08_HepaticVessel/PNG files/test/"

count = 0

for file in os.listdir(imagePath):
    # Loading nii.gz images
    img = nib.load(os.path.join(imagePath, file)) # Opening nii.gz files from the folder
    count = count + 1
    f, e = os.path.split(imagePath + file)
    # print(f + "\t" + e)
    x, y = os.path.splitext(e)
    print(str(count) + "\t" + x + "\t" + y)
    # a, b = os.path.splitext(x)
    # print(str(count) + "\t" + a + "\t" + b)
    # break
    # Reshaping 4D image into 3D
    # new_img = image.index_img(img, 0)

    # Plotting image by frontal, axial and lateral view
    plotting.plot_img(img, output_file=os.path.join(trainPath, x + ".png"))
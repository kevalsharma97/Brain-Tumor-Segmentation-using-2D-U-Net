import os
import matplotlib.image as mat
import nibabel as nib

image_path = r"D:/Segmentation/Task01_BrainTumour/imagesTr/nii_original/"   # Path to nii images
image_slice_path = r"D:/Segmentation/Brain_Images/train/slices"             # Path to store image slices

label_path = r"D:/Segmentation/Task01_BrainTumour/labelsTr/nii_original/"   # Path to nii labels
label_slice_path = r"D:/Segmentation/Brain_Images/labels/slices/"           # Path to store label slices
count = 0

for file in os.listdir(image_path):
    image = nib.load(os.path.join(image_path,file)).get_fdata()
    x, y = os.path.split(image_path + file)
    # print(x + " " + y)
    a, b = os.path.splitext(y)
    # print(a + " " + b)
    (X, Y, Z) = image.shape
    # print(image.shape)

    print("Slicing " + str(y))
    for i in range(0,X):
        imgx = image[i,:,:]
        filename = str(a) + "_x_" + str(i)
        print("Slice " + str(i) + " of x of " + str(a) + " created")
        mat.imsave(os.path.join(image_slice_path, filename + ".png"), imgx)
        i = i + 1

    print()
    for i in range(0, Y):
        imgy = image[:, i, :]
        filename = str(a) + "_y_" + str(i)
        print("Slice " + str(i) + " of y of " + str(a) + " created")
        mat.imsave(os.path.join(image_slice_path, filename + ".png"), imgy)
        i = i + 1

    print()
    for i in range(0, Z):
        imgz = image[:, :, i]
        filename = str(a) + "_z_" + str(i)
        print("Slice " + str(i) + " of z of " + str(a) + " created")
        mat.imsave(os.path.join(image_slice_path, filename + ".png"), imgz)
        i = i + 1
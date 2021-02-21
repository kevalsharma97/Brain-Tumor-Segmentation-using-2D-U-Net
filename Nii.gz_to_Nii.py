import nibabel as nib
import os
import numpy as np

sourcePath = "D:/Segmentation/Task01_BrainTumour/imagesTs/nii.gz/"
destPath = "D:/Segmentation/Task01_BrainTumour/imagesTs/nii_original/"
count = 0

for file in os.listdir(sourcePath):
    img = nib.load(os.path.join(sourcePath,file))
    # print(img.shape)
    # print(type(img))
    # print(img.header)
    # print(img.get_data_dtype() == np.dtype(np.int16))
    # print(img.affine.shape)
    # break
    count = count + 1
    f, e = os.path.split(sourcePath + file)
    x, y = os.path.splitext(e)
    print(str(count) + "\t" + x + "\t" + y)
    # new_img = image.index_img(img, 0)     # Converting 4D image to 3D if needed
    nib.save(img, os.path.join(destPath,x))
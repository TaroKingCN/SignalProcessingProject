
import cv2
import numpy as np
import os
import pandas as ps
import torch
from torch.utils.data import Dataset
import matplotlib.pyplot as plt

folder_path = '../../data/FAZ/Domain1/train/imgs'
file_names = os.listdir(folder_path)
count = 0

mask_path = '../../data/FAZ/Domain1/train/mask'
mask_name = os.listdir(mask_path)

# 创建一个5x1的子图布局
fig,axes = plt.subplots(2,5,figsize=(25,10))

for i, ax in enumerate(axes.flat):

    file_path = os.path.join(folder_path, file_names[i%5])
    mask_file_path = os.path.join(mask_path,mask_name[i%5])
    image = cv2.imread(file_path)
    mask = cv2.imread(mask_file_path)
    if i >= 5:
        ax.imshow(image+mask)
    else:
        ax.imshow(image)
    ax.set_title(f'Image {i+1}')

plt.tight_layout()
plt.show()
# for file_name in file_names:
#     if file_name.endswith('.png'):
#         file_path = os.path.join(folder_path,file_name)
#         print(file_path)
#         image = cv2.imread(file_path)
#         if count == 0:
#             print("hello")
#             cv2.imshow("Image", image)
#         count = count + 1



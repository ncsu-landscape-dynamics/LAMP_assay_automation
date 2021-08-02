# -*- coding: utf-8 -*-
"""readDNGsavePNG
"""

# Prelimns
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
#!pip install rawpy # <- Google colab format
import rawpy
#
#
# Not necessary currently. 
#import cv2
#import imageio
#import scipy.misc
#import skimage.filters
#import skimage.metrics

# Likely not needed
#from google.colab import drive
#drive.mount('/content/drive', force_remount=True)

# This may be removed. Considering whether or not to read raw image and convert
# over to tensor in this one script. Used in last block.
import torch
import torch.utils.data
import torchvision
#from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
#from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor
#from torchvision.io import read_image
#from torchvision.transforms.functional import convert_image_dtype
#import torchvision.transforms.functional as F

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Where are the new RAW images that will need to be changed before modeling?
img_dir = input("Please provide a directory path that has the images awaiting\
 analysis.\n")

if os.path.exists(img_dir) == False:
  raise TypeError("The path provided does not exist. Do you need to provide a\
  leading '/' (on Windows, you need to provide 'C:\' instead).")

print("The directory provided was {}.".format(os.getcwd()))

# Names and locations of images for reading.
rawimgs = sorted(os.listdir(img_dir))
rawimgs_dir = list()

for i in range(len(rawimgs)):
    rawimgs_dir.append(os.path.join(img_dir , rawimgs[i]))

# Read RAW images, postprocess, and check orientation.
raw_in_list = list()
post_im_list = list()

for r in range(len(rawimgs_dir)):
    raw_in_list.append(rawpy.imread(rawimgs_dir[r]))
    post_im_list.append(raw_in_list[r].postprocess(use_camera_wb=True))
    if post_im_list[r].shape[0] < post_im_list[r].shape[1]:
        post_im_list[r] = np.rot90(post_im_list[r], 3)
        print("Note: horizontal images detected. Inspect orientation.")

# Save images as PNG full-size. 
dir_save = input("Please provide a directory path for saving full-size images.\n")

if os.path.exists(dir_save) == False:
    new_dir_response = input("Directory does not exist. Should it be created? [Yes or No] If so, we will use {}\n".format(dir_save)) or "No"
    if new_dir_response == "Yes":
      os.mkdir(dir_save)
  
newnamelis = list()
save_names_path = list()

for i in range(len(rawimgs)):
    newnamelis.append(rawimgs[i].replace("dng","png"))
    save_names_path.append(os.path.join(dir_save, newnamelis[i]))
    post_im_list[i] = Image.fromarray(post_im_list[i])
    post_im_list[i].save(save_names_path[i])

# The if statement here is dodgy. An array or tensor has shape AND size. Only
# the PIL Images have only shape. Tried using type(img), but that's only for
# base types, like "str" or "int".
def centercrop(img, newsize):
    if hasattr(img, "shape"):
        height, width = img.shape[:2]   # Get dimensions
        img = Image.fromarray(img)
        print("img is tensor or np.array. widt = {}, height = {}".format(width,height))
    else:
        width, height = img.size   # Get dimensions
        print("img is PIL. widt = {}, height = {}".format(width,height))
    left = int((width - int(newsize))/2)
    top = int((height - int(newsize))/2)
    bottom = int(height - top)
    right = int(width - left)
    # Crop the center of the image
    ccrp = img.crop((left, top, right, bottom))
    return ccrp

# Crop images. 1600 x 1600
cencrop_lis = list()

for i in range(len(post_im_list)):
    cencrop_lis.append(centercrop(post_im_list[i], 1600))

# For saving the cropped images.
newnamelis = list()
crop_names_path = list()

# Save cropped images as PNG full-size. 
crop_save = input("Please provide a directory path for saving cropped images.\n")

if os.path.exists(crop_save) == False:
    new_dir_response = input("Directory does not exist. Should it be created? [Yes or No] If so, we will use {}\n".format(crop_save)) or "No"
    if new_dir_response == "Yes":
      os.mkdir(crop_save)

for i in range(len(rawimgs)):
    newnamelis.append(rawimgs[i].replace("dng","png"))
    crop_names_path.append(os.path.join(crop_save, newnamelis[i]))
    cencrop_lis[i].save(crop_names_path[i])

# Write out a bunch of plt. statements because I don't know how to call plt in a loop.
#for i in range(len(post_im_list)):
#    colus = int(len(post_im_list)/6)
#    print("plt.subplot(6,{},{})".format(colus,i+1))
#    print("plt.imshow(post_im_list[{}])".format(i))

# Optional plotting here.
#plt.figure(figsize=(40,20))

#plt.subplot(...

# Untested.
# Read raw and convert to tensor. 
#first_tensor_list = list()
#model_tensor_list = list()

#for i in range(len(cencrop_lis)):
#    tensor_list.append(torch.tensor(cencrop_lis[i]))
#    tensor_list[i] = tensor_list[i].to(device)
#    model_tensor_list[i].append(convert_image_dtype(first_tensor_list[i], dtype=torch.float))

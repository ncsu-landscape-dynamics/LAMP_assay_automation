# LAMP_assay_automation
Automate processing of images from LAMP sensors

The LAMP assay is a test used in situ on mobile phones to detect a variety of crop pathogens. Each assay produces a pair of images that has to be analyzed to ascertain infection. The analysis will be automated with machine learning and results collected and available via web services.

Some housekeeping for this repo:
-The hybridPyTorchImSeg file was testing a bunch of code. It could probably be deleted.
-Same for the imagecolorsegmentationwithopencv
-pytorch_revised is the "successful" semantic segmentation. It was only run with 19 training images. This file probably needs to be broken up into separate .py files, but I don't know how to run them as such outside of local environment.
-pytorch_finetuningimseg is what I'm currently working with for instance segmentation. 

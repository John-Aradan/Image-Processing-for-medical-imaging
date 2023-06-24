# -*- coding: utf-8 -*-
"""Graph Laplacian Operaton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14FdKNLn5aKTMLs0SQElSEEhxMboAvziR
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.io import imread
from scipy.ndimage.filters import laplace

import cv2
from IPython.display import Image, display
from matplotlib import pyplot as plt

def imshow(img, ax=None):
    if ax is None:
        ret, encoded = cv2.imencode(".jpg", img)
        display(Image(encoded))
    else:
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.axis('off')

# Load the lung nodule image
image = imread("/content/segment-R_022.png")

# Calculate the graph Laplacian operator
laplacian = laplace(image,mode='wrap', cval=10)

imshow(laplacian)

# Apply thresholding to segment the lung nodules
threshold = 110  # Adjust this threshold according to your image
segmented_image = np.where(laplacian > threshold,1,0)

# Visualize the segmentation result
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(segmented_image, cmap='gray')
ax[1].set_title('Segmented Image')
plt.show()
# -*- coding: utf-8 -*-
"""Analysis of hyperspectral images.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C_t3wT5zUOmfUvXXuGJAN1t85azedrSj
"""

!pip install spectral

from spectral import *
import matplotlib.pyplot as plt
import numpy as np
from google.colab import drive
import pandas as pd

drive.mount('/content/drive')

ruta="/content/drive/MyDrive/PRACTICA_IMAGENES"
img=open_image(ruta+"/cartagena4/cartagena4.hdr")
arr=np.asarray(img.load())
arr.shape

view = imshow(img, (29, 19, 9))

arr

df_sal=pd.read_csv("/content/drive/MyDrive/xd/coordenadas-de-agua.txt",header=None)
df_sal

arr_sal=df_sal.to_numpy()
arr_sal

l_pix_sal=[]
for pix in arr_sal:
  l_pix_sal.append(arr[pix[1],pix[0],:])

for pix in l_pix_sal:
  plt.plot(pix)
plt.grid()

arr_veg=np.asarray(l_pix_sal)
arr_veg.shape
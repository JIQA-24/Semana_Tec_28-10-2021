import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

from filtros import *

Is = Image.open('imagenes/capi.jpg');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;

k0 = sobelh()

k1 = sobelv()



J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)


plt.figure(figsize = (15,15))

plt.subplot(2,2,1)
plt.imshow(Is)
plt.xlabel('Imagen de entrada')

plt.subplot(2,2,2)
plt.imshow(J0)
plt.xlabel('Sobel Edge Horizontal')

plt.subplot(2,2,3)
plt.imshow(J1)
plt.xlabel('Sobel Edge Vertical')


plt.grid(False)
plt.show()
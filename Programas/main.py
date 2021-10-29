#importar librerias y asignarlas
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage
from filtros import *

#asignar variables y llamar a la imagen de entrada

Is = Image.open('imagenes/capi.jpg');
I = Is.convert('L'); # se convierte a escala de grises
I = numpy.asarray(I); # conversion numerica para poder operar de 0-1
I = I / 255.0; # normalizacion 0 - 1

#llamar de filtros.py y asignar un nombre

k0 = sobelh()

k1 = sobelv()

k2 = emboss()

k3 = sharpen()

k4 = passf()

#llama la operacion de convolve para realizar los despectivos kernels y filtros

J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
J2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
J3 = ndimage.convolve(I, k3, mode='constant', cval=0.0)
J4 = ndimage.convolve(I, k4, mode='constant', cval=0.0)

#Asigna un lugar para enseñar las imagenes y arregla el espacio entre cada una
#Tambien asigna el nombre correspondiente a cada una de ellas

plt.figure(figsize = (15,15))

plt.subplot(2,3,1)
plt.imshow(Is)
plt.xlabel('Imagen de entrada')

plt.subplot(2,3,2)
plt.imshow(J0)
plt.xlabel('Sobel Edge Horizontal')

plt.subplot(2,3,3)
plt.imshow(J1)
plt.xlabel('Sobel Edge Vertical')

plt.subplot(2,3,4)
plt.imshow(J2)
plt.xlabel('Emboss Filter')

plt.subplot(2,3,5)
plt.imshow(J3)
plt.xlabel('Sharpen Image')

plt.subplot(2,3,6)
plt.imshow(J4)
plt.xlabel('Pass Filter')


plt.grid(False)
plt.show()
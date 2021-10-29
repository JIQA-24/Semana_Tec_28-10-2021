# Procesador de imagens

Este es un simple repositiorio en el cual procesamos imagenes y las pasamos a travez de una serie de filtros, adicionalmente se calificara nuestro uso de github como de las branches para poder llevar a cabo el proyecto.

## Descripcion

¿Qué es un filtro o un kernel?

En pocas palabras, estas son matrices que se pueden aplicar a una imagen para aplicar efectos de imagen que se pueden realizar mediante la operación matemática conocida como convolución. Este es el proceso de agregar cada píxel de la imagen a sus vecinos locales, ponderados por el kernel.
Los valores de un píxel en la imagen resultante se calculan multiplicando cada valor de núcleo por los correspondientes valores de píxel de la imagen de entrada. Este proceso se repite hasta que el kernel haya completado la iteración de esta multiplicación en la totalidad de la imagen de entrada.

## Pre-Procesamiento y Procesamiento

### Convolución
"Convolución es el tratamiento de una matriz por otra que se llama “kernel”. El filtro matriz de convolución usa una primera matriz que es la imagen que será tratada. La imagen es una colección bidimensional de píxeles en coordenada rectágular. El kernel usado depende del efecto deseado." [-Gimp](https://docs.gimp.org/2.6/es/plug-in-convmatrix.html)

En este caso estamos ocupando la convolución para poder analizar y comprender los diferentes valor dentro de nuestra imagen.

### Padding
"La propiedad CSS padding establece el espacio de relleno requerido por todos los lados de un elemento. El área de padding es el espacio entre el contenido del elemento y su borde ( border ). No se permiten valores negativos." [-Developer Mozilla](https://developer.mozilla.org/es/docs/Web/CSS/padding)

Por otro lado Padding es un metodo opcional que se puede ocupar para poder pre-procesar las imagenes agregandoles bordes a las imagenes para que al momento en que se apliquen los filtros la imagen no se vea recortada.

## Kernels y filtros

### Sobel
El operador Sobel es utilizado en procesamiento de imágenes, especialmente en algoritmos de detección de bordes. Técnicamente es un operador diferencial discreto que calcula una aproximación al gradiente de la función de intensidad de una imagen. Para cada punto de la imagen a procesar, el resultado del operador Sobel es tanto el vector gradiente correspondiente como la norma de este vector.[De wikipedia](https://es.wikipedia.org/wiki/Operador_Sobel)

### Emboss
Emboss es una técnica de gráficos por computadora en la que cada píxel de una imagen se reemplaza por un resaltado o una sombra, dependiendo de los límites claros / oscuros de la imagen original. Las áreas de bajo contraste se reemplazan por un fondo gris. La imagen filtrada representará la tasa de cambio de color en cada ubicación de la imagen original. La aplicación de un filtro de relieve a una imagen a menudo da como resultado una imagen que se asemeja a un relieve de papel o metal de la imagen original, de ahí el nombre. [De wikipedia](https://en.wikipedia.org/wiki/Image_embossing)

### sharpen
Sharpen, que puede ayudar a enfatizar los detalles y mejorar los bordes de los objetos en una imagen, es fundamental cuando se procesan posteriormente muchos tipos de imágenes. Cabe aclarar que este proceso es muy sensible al ruido de las imagenes, es por esto que es recomendable siempre ocupar sharpen al final del procesamiento depsues de aclarar y limpiar la imagen. [-The Object](http://www.theobjects.com/dragonfly/dfhelp/4-0/Content/05_Image%20Processing/Sharpening%20Filters.htm#:~:text=The%20Unsharp%20filter%2C%20also%20called,defined%20in%20the%20original%20image.)

## main

El archivo main.py llama el archivo filtro.py el cual lleva acabo el procesamiento y filtros de las imagenes, la imagen es llamada atravez del main, recibe dichas imagenes y las plotea y enseña al usuario. -Divad Alejandro

## Filtro

Dentro de filtro se lleva acabo los kernels los cuales son aplicados a la imagen llamada en el main y las procesa, una vez que lleva acabo la funcion:
* sobelh -Divad Shriqui
* sobelb -Divad Shriqui
* emboss -Bruno Cruz 
* sharpen -Bruno Cruz

Al terminar se regresa las imagenes procesadas al archivo main

## Padding
Aqui se lleva acabo una muestra del uso de padding donde se puede observar que el contorno de la imagen no sea cortado al procesarse -Israel Quintero


## Dependencies
* numpy
* matplotlib
* scipy
* PIL

# Muestra Procesada

![Muestra](https://media.discordapp.net/attachments/615977115296202773/903727054892191824/unknown.png)

![Muestra2](https://media.discordapp.net/attachments/615977115296202773/903728553382805564/unknown.png)

### Instalar

* Descargar el github
* importar las librerias necesarias

### Como Correr el programa

1. Agregar imagenes que quieras procesar dentor de la carpeta de Imagenes
2. Abrir la consola del sistema y abrir la ruta hasta la carpeta de programas
3. Correr el programa main.py o padding.py

## Help

Si quieres cambiar la imagen que es procesada edita el main.py en la linea 9 y cambia el nombre de la imagen.
```
Is = Image.open('imagenes/mecaco.jpg');
```

Si tienes problemas adicionales al llamar la imagen o al correr no encuentra tu ruta de la imagen puedes crear la imagen en la misma carpeta de programas y solo llamar el nombre de la imagen deseada.
```
Is = Image.open('mecaco.jpg');
```


# Github 
El github fue llevado acabo atravez de 1 main y 3 branches con el nombre de cada integrante, cada integrante llevo acabo su parte en su branch, una vez el funcionamiento de esta fuera correcta se mergeo al main para su funcionamiento correcto y sin bugs

## Readme.md
Documentacion del proyecto y del github, branches creadas y mas. -Israel Quintero


## Autores

José Israel Quintero Alfaro 
A01366686@tec.mx
[Github](https://github.com/JIQA-24)

Divad Alejandor Shriqui Garrón
A01366907@tec.mx
[Github](https://github.com/Shriqui1)

Bruno Cruz Mendoza
A01367102@tec.mx
[Github](https://github.com/A01367102)


## Fuentes

Inspiration, code snippets, etc.
* [Markdown guide](https://guides.github.com/features/mastering-markdown/)
* [Padding](https://developer.mozilla.org/es/docs/Web/CSS/padding)
* [Convolución](https://docs.gimp.org/2.6/es/plug-in-convmatrix.html)

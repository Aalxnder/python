#abir y cerrar de manera automatica e archivo
# with open('Archivos1.txt','r',encoding = 'utf-8') as archivo:
#     print(archivo.readline());

from manejoArchivos import ManejoArchivos;
with ManejoArchivos("Archivos1.txt") as archivo:
    print(archivo.readline());
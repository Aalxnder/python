#debemos tener 3 clases para el catalogo de peliculas
#1. Pelicula
#2. CatalogoPeliculas
#3. test CatalogoPeliculas.py

#clase pelicula: debera tener un atributo privado llamado nombre; y un metodo str, ademas de
#el metodo setter y getter

#clase catalogo peliculas: Esta clase tiene los metodos que nos permiten interactuar con el archivo
#primero debe tener una variable static donde tendra el nombre del archivo a administrar
#despues debe tener un metodo de agregar peliculas (a)
#un metodo para listar peliculas, esto dara un listado de las peliculas
#asi como un metodo para eliminar peliculas, import os, os.remove(archivo)

#test CatalogoPeliculas.py
#este archivo es un menu con 4 opciones; con las opciones
#1. Agregar pelicula
#2. Listar peliculas
#3. Eliminar pelicula
#4. Salir
#el usuario debe elegir una opcion y se debe ejecutar la opcion elegida
class Pelicula:
    def __init__(self,nombre):
        self._nombre = nombre;
    @property
    def nombre(self):
        return self._nombre;
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
    def __str__(self):
        return self._nombre;
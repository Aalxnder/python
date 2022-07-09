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
import os;
from Peliculas import Pelicula;
class Catalogo:

    nombreArchivo = "peliculas.txt";
    def __init__(self,pelicula):
        self.pelicula = pelicula;

    def agregarpelicula(self):
        with open(self.nombreArchivo, "a",encoding = "utf-8") as archivo:
            archivo.write(str(self.pelicula) + "\n");

    def listarPeliculas(self):
        with open(self.nombreArchivo,"r",encoding = "utf-8") as archivo:
            contador = 0;
            for lista in archivo:
                print(f'[{contador}]: {lista}');
                contador += 1;

    def eliminarUnElemento(self):
        archivo = open (self.nombreArchivo,"r",encoding = "utf-8");
        lista = archivo.readlines();
        archivo.close();

        print("Lista de peliculas");
        contador = 0;
        for linea in lista:
            print(f'[{contador}]: {linea}');
            contador += 1;
        archivo.close();

        archivo = open(self.nombreArchivo,"w",encoding = "utf-8");
        pos = int(input("Ingrese el numero de la pelicula que desea eliminar: "));
        while(pos > contador):
            print("No existe un registro con ese valor");
            pos = int(input("Ingrese nuevamente el numero de la pelicula que desea eliminar: "));

        linea = lista[pos];
        lista.remove(linea);
        for linea in lista:
            archivo.write(linea);

    def eliminarArchivo(self):
        print("realmente quieres eliminar el archivo?\n");
        opc = int(input("1.Si\n2.No\n"));
        match opc:
            case 1:
                os.remove(self.nombreArchivo);
                print("Archivo eliminado");
            case 2:
                print("Archivo no eliminado");
            case _:
                print("Opcion no valida");




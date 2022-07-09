from Peliculas import Pelicula;
from catalogo import Catalogo;
import os;
import sys;

opcion = 0;
print("bienvenido al catalogo de peliculas");
print("");
bandera = True;
#funcion de agregar una pelicula
def agregarPeli():
    nombre = input("Ingrese el nombre de la pelicula: ");
    pelicula = Pelicula(nombre);
    catalogo = Catalogo(pelicula);
    catalogo.agregarpelicula();
    # menu();

#listar las peliculas
def listarPeliculas():
    catalogo = Catalogo(Pelicula(""));
    catalogo.listarPeliculas();
    # menu();

#eliminar una pelicula
def EliminarPelicula():
    catalogo = Catalogo(Pelicula(""));
    catalogo.eliminarUnElemento();
    # menu();

#funcion de eliminar el archivo completo
def EliminarArchivo():
    catalogo = Catalogo(Pelicula(""));
    catalogo.eliminarArchivo();
    # menu();

#salir
def salir():
    print("Realmente quieres salir?");
    s = int(input("1.Si\n2.No\n"));
    match s:
        case 1:
            sys.exit("Gracias por usar el catalogo");
        case 2:
            print("volviendo al menu");

#funcion del menu
def menu():
    try:
        os.system("clear");
        opc = int(input("[1] Agregar pelicula\n"+
                        "[2] Listar peliculas\n"+
                        "[3] Eliminar una pelicula\n"+
                        "[4] Eliminar todo el catalogo\n"+
                        "[5] Salir\n"));

        return opc;

    except Exception as e:
        print("no se pueden añadir caracteres no numericos o de coma flotante"+str(e));
        bandera = False;

if(bandera):
    while(opcion != ' '):

        opcion = menu();
        match opcion:
            case 1:
                agregarPeli();
            case 2:
                listarPeliculas();
            case 3:
                EliminarPelicula();
            case 4:
                EliminarArchivo();
            case 5:
                salir();
            case _:
                print("Opcion no valida");


            #fin match opcion
        #fin while opcion != ' ':
else:
    print("no se puede acceder al catalogo");

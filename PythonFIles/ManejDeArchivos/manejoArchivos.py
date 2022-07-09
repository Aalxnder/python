#clase para el manejo de archivos
#o context manager
class ManejoArchivos:
    def __init__(self,nombre):
        self._nombre = nombre;
    @property
    def nombre(self):
        return self._nombre;
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;

    def __enter__(self):
        #abrir el archivo
        print("entrando al contexto".center(50,"-"));
        self._nombre = open(self._nombre,"r",encoding = "utf-8");
        return self._nombre;
    #salir del archivo
    def __exit__(self, exc_type, exc_value, traceback):
        print("cerrando el recurso".center(50,"-"));
        #verificar si el archivo sigue abierto
        if(self._nombre):
            self._nombre.close();
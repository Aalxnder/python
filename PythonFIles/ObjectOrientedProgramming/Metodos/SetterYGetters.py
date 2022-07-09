#poner dos guiones bajos hace que no podamos modificar el acceso a un atributo fuera de la clase
#poner un guion bajo indica que no deberias poder modificar un argumento pero aun asi se puede

# una variable de solo lectura es aquella en la que noe existe el metodo setter, solo el metodo getter
# y al no poder asignar un dato por la ausencia del setter se le dice variables de solo lectura

class Persona:
    ##pasar una tupla o diccionario(primero se pasan las tuplas y despues los diccionarios
    def __init__(self,nombre,apellido,edad):
        self.__nombre = nombre;
        self.__apellido = apellido;
        self.__edad = edad;

    #metodo getter(recuperar el dato)
    @property #hace que podamos acceder a el metodo como si fuese un atributo y recuperamos el atributo
    def getNombre(self):
        print("LLamando al metodo getNombre");
        return self.__nombre;

    @getNombre.setter #definir el setter
    def setNombre(self,nombre):
        print("LLamando al metodo setNombre");
        self.__nombre = nombre;

    @property
    def getApelido(self):
        return self.__apellido;

    @getApelido.setter
    def setApellido(self,apellido):
        self.__apellido = apellido;

    @property
    def getEdad(self):
        return self.__edad;

    @getEdad.setter
    def setEdad(self,edad):
        self.__edad = edad;

    def mostrarDetalle(self):
        print(f'Persona: {self.__nombre} {self.__apellido} tiene {self.__edad} años');

    #metodo destructor
    def __del__(self):
        print(f'Eliminando persona {self.__nombre} {self.__apellido}');

# si estamos ejecutando esto desde otro archivo el nombre no sera main, asi que no se ejecutara esto;
if __name__ == '__main__':
    persona1 = Persona("Levi","Perez",18);
    persona1.setEdad = 19;
    persona1.mostrarDetalle();



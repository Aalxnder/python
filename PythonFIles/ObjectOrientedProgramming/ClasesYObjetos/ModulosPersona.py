#importar un modulo/archivo
from Metodos.SetterYGetters import Persona;

print("creacion de Objetos".center(50,'-'));
persona2 = Persona("Valeria","Gonzales",18);
persona2.mostrarDetalle();

print("Eliminacion de objetos".center(50,'-'));
del persona2;


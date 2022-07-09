
class Empleado(object):
    def __init__(self,nombre,edad,sueldo):
        self._nombre = nombre;
        self._edad = edad;
        self._sueldo = sueldo;

    def __str__(self):
        return f'Empleado: {self._nombre} edad:  {self._edad} sueldo: {self._sueldo}';

class Gerente(Empleado,object):
    def __init__(self,nombre,edad,sueldo,departamento):
        super().__init__(nombre,edad,sueldo);
        self.departamento = departamento;


    def __str__(self):
        return f'Gerente {super().__str__()} departamento: {self.departamento}';
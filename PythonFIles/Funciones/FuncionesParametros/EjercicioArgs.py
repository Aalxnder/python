# crear una funcion para sumar los valores recibidos de tipo numerico
# utilizando argumentos variables(*args) como parametro de la funcion
# y regresar como resultado la suma de todos los valores pasados como argumento

def sumar (*numeros):
    resultado = 1;
    for i in numeros:
        resultado *= i;
    return resultado;

print(sumar(3,45,6,9))
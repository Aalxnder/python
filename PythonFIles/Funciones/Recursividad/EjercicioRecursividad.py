# Imprimir los numeros de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, se debe imprimir:
# 5,4,3,2,1;
# en caso de pasar el valor 3 se debe imprimir:
# 3,2,1;
# si se pasan valores negativos no se imprime nada

def ImprimirRecursivo(numero):
    if(numero >= 1):
        print(numero);
        ImprimirRecursivo(numero-1);
    elif(numero<=0):
        print("Valor Incorrecto");
        
numero = int(input("Ingresa desde que numero comenzar a imprimir\n"));
ImprimirRecursivo(numero);
# ejercicio 1: iterar un rango de 0 a 10 e imprimir los numeros divisibles entre 2
#
# ejercicio 2: crear un rango de numeros de 2 a 6 y imprimirlos
#
# ejercicio 3; crear un rango de 3 a 10 e imprimirlos, pero con incrementos de 2 en dos

#ejercicio 1:
print("Ejercicio 1");
for i in range(10):
    if(i % 3 == 0):
        print(i);
    else:
        continue;

print("");
print("Ejercicio 2");
#ejercicio 2
for i in range(2,7):
    print(i);

print("");
print("Ejercicio 3");
for i in range(3,11,2):
    print(i);
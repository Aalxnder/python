#definir una tupla
##una tupla es inmutable, por lo cual no se puede modificar
frutas = ("Naranja","Uva","Mango","Manzana");

##si es solo un elemento en la tupla, se debe poner una coma al final del primer elemento porque si no seria solo una string
print(len(frutas));

print(frutas[0:1]); ##Inprimir las tuplas en un rango

for i in frutas: ##el ultimo indice no se incluye
    print(i,"",end=""); ##end es para que no se agregue el salto de linea por default
    print("");

##modificar los elementos de una tupla
frutaLista = list(frutas);  ##Transformar la tupla a una lista

for i in range(3):
    nuevo = input("Ingrese el valor de la lista:\n");
    frutaLista.append(nuevo);

frutas = tuple(frutaLista);
print(frutaLista);
print(frutas);

##Eliminar la tupla
del frutas;
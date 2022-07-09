#definir una lista del tipp str
nombres = ["juan","karla","Ricardo","Maria"]; #No importa el tipo

##imprimir la lista de nombres
print(nombres);

##acceder a los elementos de forma individual
print(nombres[1]);
print(nombres[2]);

#inversos
print(nombres[-1]);
print(nombres[-2]);

##acceder en un rango(no incluye el indice 2
print(nombres[0:2]);

#ir del inicio de la lista al indice sin incluirlo
print(nombres[:3]);

#Desde el indice indicado hasta el final
print(nombres[0:]);

##Cambiar valor
nombres[3] = "Fernanda";
print(nombres[0:]);

#iterar una lista
for i in nombres:
    print(i);

else:
    print("No existen mas elementos en la lista");

##preguntar los elemenos de unalista
print("Los elementos en la lista son:",len(nombres));

##agregar un elemento en la lista
nombres.append("Lorenzo");
for i in nombres:
    print(i);
else:
    print("Lista con un elemento nuevo");

##insertar un elemento en un indice especifico
nombres.insert(1,"octavio");
for i in nombres:
    print(i);

##eliminar un elemento
nombres.remove('octavio');
print("Lista sin octavio");
for i in nombres:
    print(i);

#eliminar el ultimo elemento
nombres.pop();
print("Elimina el ultimo elemento")
for i in nombres:
    print(i);

#Eliminar elemento en un indice especificado
del nombres[0];
print("");
print("Eliminar por indice");
for i in nombres:
    print(i);

#Eliminar toda la lista
print("Eliminar toda la lista");
nombres.clear()
print(nombres);

##borrar la lista de la memoria
del nombres;

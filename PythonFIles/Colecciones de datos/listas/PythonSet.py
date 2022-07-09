#no se pueden modificar los elementos, no importa el orden
# si se pueden agreagar mas o eliminar y no se pueden añadir datos repetidos

#definir elemento del tipo set
planetas = {"Jupiter","Mercurio","Marte","Venus"};
print(planetas);

print(len(planetas));

##revisar si existe un elemento
print("Marte" in planetas);

#agregar elementos
planetas.add("Tierra");
print(planetas);

#no deja repetir elemenos
planetas.add("Tierra");
print(planetas);

##eliminar un elemento posiblemente arrojando un error si no encuentra el elemento
planetas.remove("Tierra");
print(planetas);

##eliminar sin error
planetas.discard("Jupiter");
print(planetas);

#Limpiar el set por completo
planetas.clear();
print(planetas);

del planetas;
# print(planetas);
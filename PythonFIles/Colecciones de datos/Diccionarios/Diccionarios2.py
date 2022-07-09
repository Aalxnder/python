#creacion de un diccionario usando la clase dict
diccionario = dict.fromkeys(range(5),'cero');

print(diccionario);

diccionario2 = diccionario.copy();
print(diccionario2);

diccionario2[0] = 'nuevo valor';
print(diccionario2);

diccionario2[6] = 'Ana';
print(diccionario2);

##devuelve las claves, valores y ambos
print(diccionario2.keys());
print(diccionario2.values());
print(diccionario2.items());

#devuelve el valor en la posicion dada
print(diccionario2.get(1));

#devuelve las claves
print(list(diccionario2));

#devuleve un objeto iterador
print(list(iter(diccionario2)));

#devuelve la lista en reversa
print(list(reversed(diccionario2)));
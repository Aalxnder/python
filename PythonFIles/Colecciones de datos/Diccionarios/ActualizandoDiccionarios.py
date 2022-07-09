diccionario = dict(nombre='bicicleta',ruedas = 2);
print(diccionario);
diccionario['ruedas']=3 ;
print(diccionario);

diccionario2 = dict(cadena = 1,silla = 1,chasis = 1);

##Actualizando un diccionario
diccionario.update(diccionario2);
print(diccionario);

#sacando un item por valor
diccionario.pop('chasis');
print(diccionario);

#sacando el ultimo valor
diccionario.popitem();
print(diccionario);

#limpiar el diccionario
diccionario.clear();
print(diccionario);
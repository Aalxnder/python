#dicionario (key, value)

diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programing',
    'DBMS':'Database managment System'
}
print(diccionario);
##largo
print(len(diccionario));

##acceder a un elemento
print(diccionario['IDE']);

#Otra forma de recuperar un elemento
print(diccionario.get('OOP'));

##Modificando elementos
diccionario['IDE'] = 'integrated development enviroment';
print(diccionario.get('IDE'));

##Recorrer los elementos de un diccionario(keys y valores asociados a las keys)
print("");
print("Recorrer los elementos de u  diccionario");
for terminos,valor in diccionario.items():
    print(terminos,valor);

#solo recuperar las keys de el diccionario
print("");
print("recuperando las keys");
for termino in diccionario.keys():
    print(termino);

#solo recuperar los valores de el diccionario
print("");
print("recuperando los valores");
for valor in diccionario.values():
    print(valor);

##comprobar existencia de algun elemento
print('IDE' in diccionario);

print("");
print("Agregando un valor");
##agregar un elemento al diccionario
diccionario['PK'] = 'Primary Key';
print(diccionario);

#eliminar un elemento
print("");
print("Eliminando un elemento");
diccionario.pop('DBMS');
print(diccionario);

#Eliminar los elementos pero dejando la variable
diccionario.clear();
print(diccionario);

del diccionario;
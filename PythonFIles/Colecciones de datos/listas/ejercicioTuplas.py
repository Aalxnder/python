##dada la siguiente tupla
#crear una lista que solo incluya los numeros menores a 5

tupla = (13,1,8,3,2,5,8);
lista = [];

##filtrar los elementos menores a 5
for i in tupla:
    if(i < 5):
         lista.append(i);
         lista.sort();
    else:
         continue;
print(tupla);
print(lista);
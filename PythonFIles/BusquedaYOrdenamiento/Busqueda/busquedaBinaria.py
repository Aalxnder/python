##hacer una busqueda por medio de busqueda binaria;
#este metodo es mas eficiente que la bisqueda lineal

#primero ordenamos la lista;
def merge(lista1,lista2):
    #comprobar listas vacias
    lista3 = [];
    while(len(lista1) > 0 and len(lista2)>0):
        if(lista1[0]<lista2[0]):
            lista3.append(lista1[0]);
            lista1 = lista1[1:];
        else:
            lista3.append(lista2[0]);
            lista2 = lista2[1:];

    if(len(lista1) > 0):
        lista3 = lista3 + lista1;
    if(len(lista2) > 0):
        lista3 = lista3 + lista2;

    return lista3;

def mergeSort(lista):
    if(len(lista) == 1):
        return lista;

    #hayar la mitad
    lista_izq = lista[:len(lista)//2];
    lista_der = lista[len(lista)//2:];

    lista_izq = mergeSort(lista_izq);
    lista_der = mergeSort(lista_der);

    listaOrd = merge(lista_izq,lista_der);
    return listaOrd;

def BusquedaBinaria(lista,elemento):
    #inicializar inicio, medio y fin de lista
    inicio = 0;
    final = len(lista)-1;
    while inicio <= final:
        medio = (inicio + final)//2;
        #comprobar si el elemento de la lista al medio es el indice buscado

        if(lista[medio] == elemento):
            return True;
        #si es menor a el elemento que buscamos, si siguiente sera el nuevo inicio

        elif(lista[medio] < elemento):
            inicio = medio +1;
        #si es mayor al elem buscado el final sera, el indice de en medio -1
        elif(lista[medio] > elemento):
            final = medio -1;

    return False;

cant = int(input("Ingresa la cantidad de valores: "));
lista = [];
for i in range(cant):
    valores = int(input(f'ingresa el valor {i}: '));
    lista.append(valores);

print(mergeSort(lista));
Elemento = int(input("ingresa el elemento a buscar: "));

print(BusquedaBinaria(lista,Elemento));



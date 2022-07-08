#merge sort con cadena
def merge(lista1,lista2):
    lista3 = [];
    while(len(lista1) > 0 and len(lista2) > 0):
        if(lista1[0] < lista2[0]):
            lista3.append(lista1[0]);
            lista1 = lista1[1:];

        else:
            lista3.append(lista2[0]);
            lista2 = lista2[1:];

    if(len(lista1) > 0):
        lista3 = lista3+lista1;
    if(len(lista2) > 0):
        lista3 = lista3+lista2;

    return lista3;

def mergeSort(lista):
    if len(lista) == 1:
        return lista;

    lista_izq = lista[:len(lista)//2]; #tomar valores desde el inicio hasta la mitad
    lista_der = lista[len(lista)//2:]; #lo mismo pero con la derecha

    ##llamar funcion mergesort
    lista_izq = mergeSort(lista_izq);
    lista_der = mergeSort(lista_der);

    listaOrdenada = merge(lista_izq,lista_der);
    return listaOrdenada;

cadena = input("Ingresa cualquier cadena para ordenar sus caracteres:\n");
lista = [];
for i in cadena:
     lista.append(i);

print(lista);

print(mergeSort(lista));
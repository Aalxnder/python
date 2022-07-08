#algoritmo mergeSort

def merge(lista1,lista2):
    lista3 = [];
    while(len(lista1) > 0 and len(lista2) > 0):
        if(lista1[0] < lista2[0]):
            lista3.append(lista1[0]);
            lista1 = lista1[1:];

        else:
            lista3.append((lista2[0]));
            lista2 = lista2[1:];

    if(len(lista1) >0):
        lista3 = lista3 + lista1;
    if(len(lista2) > 0):
        lista3 = lista3 + lista2;

    return lista3;


def mergeSort(lista):
    #caso base (revisar si la longitud de la lista es igual a 1)
    if len(lista) == 1:
        return lista;
    #caso recursivo(encontrar el punto medio)
    lista_izq = lista[:len(lista)//2];
    lista_der = lista[len(lista)//2:];

    lista_izq = mergeSort(lista_izq);
    lista_der = mergeSort(lista_der);

    listaOrdenada = merge(lista_izq,lista_der);

    return listaOrdenada;

cant = int(input("Ingresa la cantidad de valores a ordenar:\n"));
lista = [];
for i in range(cant):
    valores = int(input(f'Ingresa el valor {i}: '));
    lista.append(valores);

print(lista);
print(mergeSort(lista));



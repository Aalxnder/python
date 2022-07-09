#Si no sabemos la cantidad de elementos a pasar se pone el *
def ListarNombres(*nombres): #Python transforma esto a una tupla
    for i in nombres:
        print(i);

ListarNombres("Alexander","Azalia","Perla","Dulce","Valeria","Levi");
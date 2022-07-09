# en este ejemplo se ve como una misma definicion se puede ver como una misma definicion
# de funcion puede hacer diferentes logicas utilizando las funciones externas que se pasan
# como parametros

import math;
def raiz_de_par(x):
    if(not x%2):
        return math.sqrt(x);

def mul_de_par(x,multi=5):
    if(not x % 2):
        return x*multi;

def aplicar_Funtion(lst,func):
    return [func(x) for x in lst];

print(aplicar_Funtion(range(20),mul_de_par));

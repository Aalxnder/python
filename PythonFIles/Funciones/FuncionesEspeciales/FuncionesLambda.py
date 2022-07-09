import math;

def identidad(x):
    return x;
lambda x: x;

f_x3 = lambda x: x**3;

print(f_x3(10));
print(f_x3(20));
lst = ['a1','a14','a2','a3','a4','a5','a6','a7','a8','a9','a10','a200','a12','a13'];
print(lst);
# sorted(lst); #ordenacion por caracter
# print(lst);

#ordenacion numerica
print(sorted(lst, key = lambda x: int(x[1:])));
# print(lst); #lista ordenada por numero

lst2 = [1,453,553,34,23,7];
lst2.sort(key = lambda x:(x<400,x)); ##ordenacion de varios parametros usando tuplas
print(lst2);

print(min(lst2));
print(min(lst2,key = lambda x: x<50))

print(max(lst2))

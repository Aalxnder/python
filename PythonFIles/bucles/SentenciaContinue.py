# for i in range (6):
#     if(i % 2 == 0):
#         print(f'El valor {i} es un numero par');

for i in range(6):
    if(i % 2 != 0):
        continue; ##esto ya no ejecuta ninguna de as lineas siguientes, solo sigue con otra iteracion
    print(f'Valor: {i}');
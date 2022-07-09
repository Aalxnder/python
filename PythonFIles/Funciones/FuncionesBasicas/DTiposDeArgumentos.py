def DesplegarNombres(nombres):
    for nombre in nombres:
        print(nombre);

nombres = [];
for i in range(0,3):
    nombre = input("Ingresa un nombre\n");
    nombres.append(nombre);

DesplegarNombres(nombres);
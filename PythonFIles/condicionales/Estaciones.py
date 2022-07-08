mes = int(input("Ingresa el numero segun el mes elegido(1-12)\n"));
estacion = None;
while(mes >12 or mes <=0):
    print("Ingresa un mes valido...");
    mes = int(input("Ingresa nuevamente el numero segun el mes elegido(1-12)\n"));

if((mes == 1) or (mes == 2) or (mes ==12)):
    estacion = "Invierno";
    print(f'la estacion del mes {mes} es {estacion}');
elif((mes == 3)or(mes == 4)or(mes == 5)):
    estacion = "Primaveria";
    print(f'la estacion del mes {mes} es {estacion}');
elif((mes == 6)or(mes == 7)or(mes == 8)):
    estacion = "Verano";
    print(f'la estacion del mes {mes} es {estacion}');
elif((mes == 9)or(mes == 10)or(mes == 11)):
    estacion = "Verano";
    print(f'la estacion del mes {mes} es {estacion}');
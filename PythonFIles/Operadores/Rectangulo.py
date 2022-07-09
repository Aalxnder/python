#
#Calcular el area y perimetro de un rectangulo
#el user debe poner el alto y ancho y calcular y mostrar los valores
ancho = int(input("Ingresa el ancho del rectangulo\n"));
largo = int(input("Ingresa el largo del rectangulo\n"));

area = ancho*largo;
perimetro = (ancho+largo)*2;

print(f'el area del rectangulo es {area}');
print(f'El perimetro del rectangulo es {perimetro}');
numero = int(input("ingresa un valor entre 1 y 3:\n"));
while((numero != 1)and(numero != 2)and(numero != 3)):
    print("Ingresa un numero valido:");
    numero = int(input("ingresa un valor entre 1 y 3:\n"));

if(numero == 1):
    numeroTexto = "Numero uno";
elif(numero == 2):
    numeroTexto = "Numero dos";
elif(numero == 3):
    numeroTexto = "Numero tres";

print(f'Numero proporcionado {numero}: {numeroTexto}');
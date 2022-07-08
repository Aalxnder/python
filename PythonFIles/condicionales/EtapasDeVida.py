edad = int(input("Ingresa tu edad:\n"));
while(edad<0 or edad>30):
    print("Error, ingresa una edad valida:");
    edad = int(input("Ingresa nuevamente tu edad:\n"));
if(edad >= 0 and edad <=10):
    print("La infancia es increible");
elif(edad > 10 and edad <=20):
    print("Muchos cambios, mucho estudio");
elif(edad >20 and edad <=30):
    print("Amor y comienza el jale");

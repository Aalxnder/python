#Calcular el volumen de un cubo

class CuboVolumen:
    def __init__(this,base,altura,profundidad):
        this.base = base;
        this.altura = altura;
        this.profundidad = profundidad

    def volumen(this):
        return (this.base*this.altura)*this.profundidad;

base = float(input("Ingresa la base del cubo:\n"));
altura = float(input("Ingresa la altura del cubo:\n"));
profundidad = float(input("Ingresa la profundidad del cubo\n"));

##creacion de objeto
cubo = CuboVolumen(base,altura,profundidad);
print(f'Volumen del cubo: {cubo.volumen():.2f} metros cubicos');

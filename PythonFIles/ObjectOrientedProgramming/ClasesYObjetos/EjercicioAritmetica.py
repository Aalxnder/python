##realizar las operaciones de suma, resta ,division y multiplicacion

class Aritmetica:
    """
        Clase aritmetica para realizar las operaciones de suma, resta ,division y multiplicacion
    """
    def __init__(this,numero1,numero2):
        this.numero1 = numero1;
        this.numero2 = numero2;

    def suma(this):
        return this.numero1 + this.numero2;

    def resta(this):
        return this.numero1 -this.numero2;

    def multiplicar(this):
        return this.numero1 * this.numero2;

    def dividir(this):
        return this.numero1/this.numero2;

num1 = float(input("Ingresa el primer numero\n"));
num2 = float(input("Ingresa el segundo numero\n"));

operacion = Aritmetica(num1,num2);

print(f'suma: {operacion.suma():.2f}');
print(f'resta: {operacion.resta():.2f}');
print(f'Multiplicacion: {operacion.multiplicar():.2f}');
print(f'Division: {operacion.dividir():.2f}');


def operar(num1,num2,func):
    return func(num1,num2);

def suma(num1,num2):
    return num1+num2;

def resta(num1,num2):
    return num1-num2;

def multiplicacion(num1,num2):
    return num1*num2;

def division(num1,num2):
    try:
        return num1/num2;
    except ZeroDivisionError as e:
        return "No se puede dividir por cero: ",e;

print(operar(10,10,suma));
print(operar(10,10,resta));
print(operar(10,10,multiplicacion));
print(operar(10,0,division));
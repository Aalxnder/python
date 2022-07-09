resultado = None;
from ExcepcionesPropias import numerosIguales;
try:
    a = int(input("Ingrese un numero: "));
    b = int(input("Ingrese otro numero: "));
    #lanzar una excepcion propia
    if(a == b):
        raise numerosIguales("Los numeros son iguales");
    resultado = a/b;
except ZeroDivisionError as e:
    print(f"ocurrio un error: {e}");

except Exception as e:
    print(f"ocurrio un error: {e}");
else:
    print("No se arrojo una excepcion");
finally:
    print("Se ejecuta el finally");
print(resultado);
print("saliendo de la excepcion");
num1 = int(input("Ingresa el primer numero:\n"));
num2 = int(input("Ingresa el segundo numero:\n"));

if(num1 > num2):
    print(f'el numero {num1} es mayor que el numero {num2}');
elif(num1 == num2):
    print(f'el numero {num1} y el numero {num2} son iguales');
else:
    print(f'el numero {num2} es mayor que el numero {num1}');
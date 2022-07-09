# Conversor de temperatura
# realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
# (10 °C × 9/5) + 32 = 50

def CelsiusAFahrenheit(celcius):
    GradosFahrenheit = ((celcius*9)/5)+32;
    return GradosFahrenheit;

def FahrenheitACelsius(Faherenheit):
    GradosCelsius = ((Faherenheit-32)*5)/9;
    return GradosCelsius;

Celsius = float(input("Ingresa los grados celsius a convertir a fahrenheit\n"));
ConversionFahrenheit = CelsiusAFahrenheit(Celsius);

fahrenheit = float(input("Ingresa los grados fahrenheit a convertir a celsius\n"));
ConversionCelsius = FahrenheitACelsius(fahrenheit);
print(f'{fahrenheit} grados fahrenheit son {ConversionCelsius}');
print(f'{Celsius} grados Celsius son {ConversionFahrenheit}');


try:
    archivo = open("Archivos1.txt","a",encoding = "utf-8");
    texto = input("ingresa algo para llenar el archivo: ");
    archivo.write(texto + "\n");
except Exception as e:
    print("Error al abrir el archivo"+str(e));
finally:
    archivo.close();
    print("Archivo cerrado");
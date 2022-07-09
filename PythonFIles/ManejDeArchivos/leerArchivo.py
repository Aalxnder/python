try:
    #leer todo el archivo
    archivo = open("Archivos1.txt","r",encoding="utf-8");
    # texto = archivo.read();
    # print(texto);

    # #leer solo algunos caracteres
    # print(archivo.read(10));
    # print(archivo.read(5));

    #leer lineas completas
    # print(archivo.readline());
    # print(archivo.readline());

    #iterar el archivo
    # for linea in archivo:
    #     print(linea);
    #
    # #leer todas las lineas(devuelve una lista)
    # print(archivo.readlines());

    #acceder a una linea de la lista
    # print(archivo.readlines()[1]);

    #copiar un archivo a otro
    copia = open("copia.txt","a",encoding = "utf-8");
    copia.write(archivo.read());
    archivo.close();
    copia.close();
    print("Archivo copiado");
except Exception as e:
    print("Error al abrir el archivo"+str(e));
finally:
    archivo.close();
    print("Archivo cerrado");
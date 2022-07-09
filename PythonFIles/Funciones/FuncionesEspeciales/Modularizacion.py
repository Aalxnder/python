# partiendo de una cadena de caracteres,se pretende separar
# la cadena mediante un separador y aplicar una funcion basada en el algoritmo
# de cifrado md5 a cada elemento para obtener su forma exadecimal, una vez optenida
# se gurada en un fichero de texto plano:
# import hashlib
#
#
# def extraerTexto(cadenaOriginal,sep= " "):
#     return cadenaOriginal.split(sep);
#
# def aplicarhash(lst):
#     mds5 = [];
#     for cad in lst:
#         m = hashlib.md5(cad.encode('utf-8'));
#         mds5.append(m.hexdigest())
#     return mds5;
#
# def escribirFichero(data,nombreFichero = 'out.txt'):
#     with open(nombreFichero, 'w') as f:
#         for d in data:
#             f.write(d+ '\n');
#         return nombreFichero;
#
# cadenaOriginal = input("Ingrese una cadena");
# identificadores = extraerTexto(cadenaOriginal,sep = '<>');
# idModificados = aplicarhash(identificadores);
# nombreFichero = escribirFichero(idModificados);
#


#Formato Json
import hashlib
import json

def extraerTexto(cadenaOriginal,sep= " "):
    return cadenaOriginal.split(sep);

def hashList(lst):
    Hashes = [];
    for cad in lst:
        m = hashlib.sha256();
        m.update(cad.encode('utf-8'));
        Hashes.append(m.hexdigest())
    return Hashes;

def escribirJson(data,nombreFichero = 'Out-Json'):
    with open(nombreFichero, 'w') as f:
        json.dump(data,f)
    return nombreFichero;

cadenaOriginal = input("Ingrese una cadena\n");
identificadores = extraerTexto(cadenaOriginal,sep = '<>');
idModificados = hashList(identificadores);
nombreFichero = escribirJson(idModificados);
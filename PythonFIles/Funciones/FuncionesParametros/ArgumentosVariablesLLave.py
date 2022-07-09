#Esta funcion puede recibir diccionarios
def ListarTerminos(**Terminos):
    for llave, valor in Terminos.items():
        print(f'llave: {llave}, Valor: {valor}');

ListarTerminos(IDE = 'Integrated Development Enviroment',
               PK = 'Primary Key',
               BDMS = 'Database Managment System');

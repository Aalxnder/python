#crear funciones dentro de funciones, en laqs cuales guradaremos un numero de telefono
def prefijo(numprefijo):
    def numero(numero):
        return f'{numprefijo} {numero}';
    return numero;

telefonoMexico = prefijo('+52');
# telefonoMexico(3322895914);
print(telefonoMexico(3322895914));
import random;
import string;

class IteradorPersonalizado:
    def __init__(this,max_elementos,opciones = string.ascii_letters):
        this.max_elementos = max_elementos;
        this.indice_iterador = 0;
        this.opciones=opciones;

    def __iter__(this):
        return this;

    def __next__(this):
        if(this.indice_iterador >= this.max_elementos):
            raise StopIteration();
        else:
            this.indice_iterador += 1;
            return random.choice(this.opciones);

print(list(IteradorPersonalizado(10)));


class Fibonacci:
    def __init__(this):
        this.idx = 2;
        this.v_previo = 0; #primer valor
        this.v_actual = 1; #segundo valor

    def __iter__(this):
        return this;

    def __next__(this):
        this.idx +=1;
        v_previo = this.v_previo; ##guardar el valor actual
        this.v_previo = this.v_actual;
        this.v_actual = this.v_actual + v_previo;
        return this.idx,this.v_actual; #Devuelve la tupla (posicion,valor)

iter_fibo = Fibonacci(); #Creo el objeto

print(next(iter_fibo)) #valor en la tercera posicion

print(next(iter_fibo)) #valor en la 4ta posicion

iter_fibo = Fibonacci(); #Creo el objeto
valoresfibo = [];
for i in range(15):
    valoresfibo.append(next(iter_fibo));

print(valoresfibo);


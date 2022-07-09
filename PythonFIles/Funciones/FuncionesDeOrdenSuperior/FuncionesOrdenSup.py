# En la programacion funcional existe el concepto de funciones de orden superior
# ,se trata de funciones que aceptan otras funciones como parametros y que python las soporta sin problemas
def op(a,b,funct):
    return funct(a,b);
print(op(2,3,lambda x,y: x+y));

print(op(2,3,lambda x,y: x*y));

print(op("Pedro"," perez",lambda x,y: x+y));
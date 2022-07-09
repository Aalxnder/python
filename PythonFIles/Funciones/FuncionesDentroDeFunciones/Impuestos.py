def beneficios(gastos:list, ingresos:list, tramosImpuestos):
    def ObtenerImpuesto(ingreso):
        impuestoActual = tramosImpuestos[0][1];
        for hastaValor,impuesto in tramosImpuestos:
            if(hastaValor > ingreso):
                break;
            else:
                impuestoActual = impuesto;
        return impuestoActual;

    def CalculoNeto(ingresoBruto):
        impuesto = ObtenerImpuesto(ingresoBruto);
        return ingresoBruto -(ingresoBruto * impuesto);

    gastosTotales = sum(gastos);
    ingresosNetos = sum(map(CalculoNeto,ingresos));
    return ingresosNetos -gastosTotales;

gastos = [22,314,32,52];
ingresos = [45,623,12,90];
tramosImpuestos = [(20,0.06),(50,0.08),(200,0.1),(500,0.2),(float("inf"),0.21)];
print(beneficios(gastos,ingresos,tramosImpuestos));
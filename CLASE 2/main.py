from Indicadores import *
valor = float(input('ingrese el valor que dolares que quiere convertir: ')) 

i = Indicadores()
resultado = float(i.indicadoresEconomicos())*valor
print(resultado)




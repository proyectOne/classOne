'''
from empleado import Empleado

e1= Empleado()
e1.setNombre("Moises")
e1.apellido = "Rey"
e1.cargo = "Estudiante"
e1.sueldo = "300"
print(e1)
'''
from nomina import Nomina

nominas =[]
while True:
    print("1. ingrese nomina: ")
    print("2. salir ")
    opcion = input("ingrese la opcion: ")

    if opcion =='1':
        renglon =[]

        n = Nomina()
        salario = float(input("Ingrese el sueldo basico: "))
        diasL = float(input("Ingrese el numero de dias: "))
        print(salario)
        print (diasL)
        n.setSalariobasico(salario)
        n.setdiasliquidados(diasL)

        #renglon.append({n.getSalariobasico})
        renglon.append({'variable': 'salario basico ','Resultado':n.getSalariobasico()})
        #renglon.append(n.getdiasliquidados)
        renglon.append({'variable': 'dias liquidados','Resultado':n.getdiasliquidados()})
        #renglon.append(n.salariodevengado)
        renglon.append({'variable': 'salario devengado','Resultado':n.salariodevengado()})
        #renglon.append(n.auxilioTransporte)
        renglon.append({'variable': 'auxilio de tranporte','Resultado':n.auxilioTransporte()})
        #renglon.append(n.totaldevengado)
        renglon.append({'variable': 'totaldevengado','Resultado':n.totaldevengado()})
        #renglon.append({'variable': '','resultado':})
        nominas.append(renglon)

    elif opcion == "2":
        print("saliendo")
        break

f = open('nominas.txt', 'w')

for i in nominas:
    f.write('*********************************************\n') 
    for j in i:
        f.write(str(j)+ '\n')
f.close()



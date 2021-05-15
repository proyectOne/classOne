from tkinter import *
from empleado import Empleado
from nomina import Nomina


class Ejercicio1:
    def frame(self):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        frame.config(bg="blue")
        frame.config(width=480,height=400)

        root.mainloop() 
class Ejercicio2:
    def label1(self):
        root =Tk()
        Label(root,text ="hola mundo").pack()
        Label(root,text ="hola mundo 2").pack()
        Label(root,text ="ultimo label").pack()

        labeldif = Label(root , text="label diferente")
        labeldif.pack(anchor=CENTER)
        labeldif.config(
                        fg="blue",
                        bg="red",
                        font=("verdana", 24))
        root.mainloop()

class Ejercicio3:
    def inputText(self):
        
        root = Tk()

        frame = Frame(root)
        frame.pack()
        entry = Entry(frame)
        entry.pack(side=RIGHT)

        label = Label(frame ,text= "Nombre de empleado")
        label.pack(side =LEFT)



        frame1 = Frame(root)
        frame1.pack()
        entry1 = Entry(frame1)
        entry1.pack(side=RIGHT)

        label1 = Label(frame1,text= "Nombre de empleado")
        label1.pack(side =LEFT) 
        
        frame2 = Frame(root)
        frame2.pack()
        entry2 = Entry(frame2)
        entry2.pack(side=RIGHT)

        label2 = Label(frame2,text= "Cargo")
        label2.pack(side =LEFT) 

        root.mainloop()


    def textarea(self):
        root = Tk()

        texto = Text(root)
        texto.pack()


        root.mainloop()



class inputText2:
    def inputText(self):
        
        root = Tk()

        label = Label(root ,text= "Nombre")

        label.grid(row=0,column=0)

        entry = Entry(root)
        entry.grid(row=0,column=1)

        label1 = Label(root ,text= "Apellido")

        label1.grid(row=1,column=0)

        entry1 = Entry(root)
        entry1.grid(row=1,column=1)

        label2 = Label(root ,text= "Cargo")

        label2.grid(row=2,column=0)

        entry2 = Entry(root)
        entry2.grid(row=2,column=1)





        root.mainloop()


class calculadora:


    r=None
    N1=None
    N2=None


    def sumar(self):

        resultado = float(self.N1.get()) + float(self.N2.get())
        self.r.set(resultado)
        self.limpiar()

    def limpiar(self):
        self.N2.set("")
        self.N1.set("")


    def inicio(self):
        root =Tk()

        self.r= StringVar()
        self.N1= StringVar()
        self.N2= StringVar()
        root.config(bd=15)
        Label(root, text="Numero 1").pack()
        Entry(root , justify=CENTER , textvariable=self.N1).pack()


        Label(root, text="\nNumero 2").pack()
        Entry(root , justify=CENTER, textvariable=self.N2).pack()


        Label(root, text="\nResultado").pack()
        Entry(root , justify=CENTER, textvariable=self.r).pack()

        Label(root).pack() #separador
        Button(root, text="Sumar", command=self.sumar).pack()

        root.mainloop()

class interfazNomina:
    def __init__(self):
        self.root=Tk()
        self.root.config(bd=15)
        self.nombres=StringVar()
        self.apellidos=StringVar()
        self.cargo=StringVar()
        self.salario=StringVar()
        self.dias=StringVar()
        self.nomina = Nomina()
        self.texto = Text(self.root)


    def agregarEmpleado(self):

        empleado= Empleado()
        empleado.setNombre(self.nombres.get())
        empleado.setApellido(self.apellidos.get())
        empleado.setCargo(self.cargo.get())
        empleado.setSalario(self.salario.get())

        self.nomina.setSalariobasico(float(self.salario.get()))
        self.nomina.setdiasliquidados(float(self.dias.get()))

        self.limpiar()
        self.texto.insert('insert', '\n++++++++++++++++++++++++++++++++++++++++\n')
        self.texto.insert('insert', empleado)
        self.texto.insert('insert', '\n++++++++++++++++++++++++++++++++++++++++\n')
        self.texto.insert('insert', self.nomina)

        print(empleado)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(self.nomina)

    def limpiar(self):
        self.nombres.set("")
        self.apellidos.set("")
        self.cargo.set("")
        self.salario.set("")
        self.dias.set("")

    def interfaz(self):
        frame =Frame(self.root,width=480,height=320)

        label = Label(frame,text= "Nombre",)
        label.grid(row=0,column=0)
        entry = Entry(frame, textvariable= self.nombres)
        entry.grid(row=0,column=1)
        ####################################################
        label1 = Label(frame ,text= "Apellido")
        label1.grid(row=1,column=0)
        entry1 = Entry(frame, textvariable= self.apellidos)
        entry1.grid(row=1,column=1)
        ####################################################
        label2 = Label(frame ,text= "Cargo")
        label2.grid(row=2,column=0)
        entry2 = Entry(frame,textvariable= self.cargo)
        entry2.grid(row=2,column=1)
        ####################################################
        label2 = Label(frame ,text= "Salario")
        label2.grid(row=3,column=0)
        entry2 = Entry(frame,textvariable= self.salario)
        entry2.grid(row=3,column=1)
        ####################################################
        label2 = Label(frame ,text= "Dias Devengados")
        label2.grid(row=4,column=0)
        entry2 = Entry(frame,textvariable = self.dias)
        entry2.grid(row=4,column=1)
        ####################################################
        agregar = Button(frame, text="Agregar", command=self.agregarEmpleado)
        agregar.grid(row=5,column=1)

        
        frame.pack(fill='both',expand=1)
        self.texto.pack(fill='both', expand=1)

        self.root.mainloop()



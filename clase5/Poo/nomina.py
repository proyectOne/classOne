from Indicadores import indicadores

class Nomina(indicadores):

    def __init__(self):
        self.__salarioBasico = 0
        self.__diasliquidados = 0
        self.__smlv = 908526
        self.__auxilio =106454




    def setSalariobasico(self, salarioBasico):
        if(str(type(salarioBasico))== "<class 'int'>" or str(type(salarioBasico))== "<class 'float'>" ):
            if salarioBasico >= self.__smlv:
                self.__salarioBasico =salarioBasico
            else:
                print('el salario basico no puede ser menor a el SMLV')

            self.__salarioBasico = salarioBasico
        else:
            print('error')
        self.__salarioBasico = salarioBasico

    def getSalariobasico(self):
        return self.__salarioBasico

    def getdiasliquidados(self):
        return self.__diasliquidados
    def setdiasliquidados(self, diasliquidados):
        self.__diasliquidados = diasliquidados

    def salariodevengado(self):
        try:
            return (self.__salarioBasico/30)* self.getdiasliquidados()
        except Exception as e:
            print(e)
            print("error al calcular el salario Devengado")

    def auxilioTransporte(self):
        if self.__salarioBasico >=(2*self.__smlv):
            return 0
        else:
            return self.__auxilio/30 * self.__diasliquidados
    def totaldevengado(self):
        return self.salariodevengado() + self.auxilioTransporte()
    def __str__(self):
        return str ("salario basico {}\n"
                    "dias liquidados {}\n"
                    "salarios devengado {}\n"
                    "Auxilio de transporte {}\n"
                    "total devengado {}").format(
                        self.__salarioBasico,
                        self.__diasliquidados,
                        self.salariodevengado(),
                        self.auxilioTransporte(),
                        self.totaldevengado()
                    )

    

    



class Empleado:
    def __init__(self):
        self.__nombre=None
        self.__apellido=None
        self.__cargo=None
        self.__sueldo=None



    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getCargo(self):
        return self.__cargo

    def getSalario(self):
        return self.__sueldo



    def setNombre(self,nombre):
        self.__nombre=nombre



    def setApellido(self,apellido):
        self.__apellido=apellido


    def setCargo(self,cargo):
        self.__cargo=cargo

    def setSalario(self,sueldo):
        self.__sueldo=sueldo

    def __str__(self):
        return str(
             "Nombre: {} \n"
             "Apellido: {} \n"
             "Cargo: {} \n"
             "Sueldo: {} \n"
        ).format(
            self.__nombre,
            self.__apellido,
            self.__cargo,
            self.__sueldo
        )
from base import DataBase
from datetime import datetime

class Prestamo(DataBase):
    
    def __init__(self, id_prestamo=0, fecha_inicio=None, fecha_devolucion=None, id_user=0, id_encargado=0, multa_total=None) -> None:
        super().__init__()
        self.__id_prestamo = id_prestamo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_devolucion = fecha_devolucion
        self.__id_user = id_user
        self.__id_encargado = id_encargado
        self.__multa_total = multa_total
    
    # Getters    
    def getIdPrestamo(self):
        return self.__id_prestamo
    
    def getFechaInicio(self):
        return self.__fecha_inicio
    
    def getFechaDevolucion(self):
        return self.__fecha_devolucion
    
    def getIdUser(self): 
        return self.__id_user
    
    def getIdEncargado(self): 
        return self.__id_encargado
    
    def getMultaTotal(self):
        return self.__multa_total
    
    # Setters
    def setFechaInicio(self, newFechaInicio):
        self.__fecha_inicio = newFechaInicio
        self.updatePrestamo()
        return True

    def setFechaDevolucion(self, newFechaDevolucion):
        self.__fecha_devolucion = newFechaDevolucion
        self.updatePrestamo()
        return True
    
    # Funciones a través de consultas
    def getPrestamo(self):
        data = ""
        sql = "SELECT id_prestamo, fecha_inicio, fecha_devolucion, id_user, id_encargado, multa_total FROM `prestamo`;"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            prestamos = []
            for value in data:
                prestamo = Prestamo(value[0], value[1], value[2], value[3], value[4], value[5])
                prestamos.append(prestamo)
            self.prestamos = prestamos
            return prestamos
        except Exception as e:
            raise
            
    def newPrestamo(self):
        fechaInicio = self.getFechaInicio()
        fechaDevolucion = self.getFechaDevolucion()
        id_user = self.getIdUser()
        id_encargado = self.getIdEncargado()
        
        sql = "INSERT INTO `prestamo` (`fecha_inicio`, `fecha_devolucion`, `id_user`, `id_encargado`) VALUES ('{}', '{}', {}, {})".format(fechaInicio, fechaDevolucion, id_user, id_encargado)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False

    def updatePrestamo(self):
        id_prestamo = self.getIdPrestamo()
        fecha_inicio = self.getFechaInicio()
        fecha_devolucion = self.getFechaDevolucion()
        id_user = self.getIdUser()
        id_encargado = self.getIdEncargado()
        
        sql = "UPDATE `prestamo` SET `fecha_inicio`='{}', `fecha_devolucion`='{}', `id_user`={}, `id_encargado`={} WHERE `id_prestamo`={}".format(fecha_inicio, fecha_devolucion, id_user, id_encargado, id_prestamo)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False
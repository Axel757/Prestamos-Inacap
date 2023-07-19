from base import DataBase
from datetime import date

class Prorroga(DataBase):
    
    def __init__(self,prorroga_id=0,fecha_inicio=None,fecha_termino=None,prestamo_id=0) -> None:
        super()._init_()
        self.__prorroga_id= prorroga_id
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__prestamo_id = prestamo_id
    
    
    #Getters    
    def getProrrogaid(self):
        return self.__prorroga_id
    def getPrestamoid(self): 
        return self.__prestamo_id
    def getFechainicio(self):
        return self.__fecha_inicio
    def getFechatermino(self):
        return self.__fecha_termino
    #########################################################
    
    #Setters
    
    def setFechainicio(self,newFechainicio):
        self.__fecha_inicio = newFechainicio
        self.updateFechainicio()
        return True

    def setFechatermino(self,newFechatermino):
        self.__fecha_termino = newFechatermino
        self.updateUser()
        return True
    
    ################################################
    
    #funciones a traves de consultas
    def newProrroga(self,prorroga):
        fechaInicio = prorroga.getFechainicio()
        fechaTermino = prorroga.getFechaTermino()
        prestamo_id = self.getPrestamoId()
        
        sql="INSERT INTO `prorroga`( `fecha_inicio`, `fecha_termino`, `pretamo_id`) VALUES ('{}', '{}', {})".format(fechaInicio, fechaTermino, prestamo_id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error : "+str(e.args))
            self.connection.close()
        return False

    def getProrroga(self):
        
        data = ""
        sql = "SELECT prorroga_id, fecha_inicio, fecha_termino, prestamo_id FROM `prorroga`;"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            prorrogas = []
            for value in data:
                prorroga= Prorroga(value[0],value[1],value[2],value[3])
                prorrogas.append(prorroga)
            self.prorrogas=prorrogas
            return prorrogas
        except Exception as e:
            raise
        
    def updateProrroga(self):
        prorroga_id = self.getProrrogaid()
        fecha_inicio = self.getFechainicio()
        fecha_termino = self.getFechatermino()
        prestamo_id = self.getPrestamoid()
        
        sql = "UPDATE `prorroga` SET `fecha_inicio`='{}', `fecha_termino`='{}', `prestamo_id`={} WHERE `prorroga_id`={}".format(fecha_inicio, fecha_termino, prestamo_id, prorroga_id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False       



from base import DataBase

class Usuario(DataBase):
    def __init__(self,id=0,rut="",nombre="",telefono ="",email = "",docente = False) -> None:
        super().__init__()
        self.__id = id
        self.__rut = rut
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__docente = docente

    def getId(self):
        return self.__id
    def getRut(self):
        return self.__rut
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getEmail(self):
        return self.__email
    def getDocente(self):
        if self.__docente==True:
            return 1
        else:
            return 0
        

    def setNombre(self,newNombre):
        self.__nombre = newNombre
        self.updateUser()
        return True

    def setTelefono(self,newTelefono):
        self.__telefono = newTelefono
        self.updateUser()
        return True

    def setEmail(self,newEmail):
        self.__email = newEmail
        self.updateUser()
        return True

    def setDocente(self,newEstadoDocente):
        self.__docente = newEstadoDocente
        self.updateUser()
        return True
    
    def newUser(self,user):
        rut = user.getRut()
        nombre = user.getNombre()
        telefono = user.getTelefono()
        email = user.getEmail()
        docente = user.getDocente()
        sql="INSERT INTO `usuario`( `rut`, `nombre`, `telefono`, `email`, `docente`) VALUES ('{}','{}','{}','{}',{})".format(rut,nombre,telefono,email,docente)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            exito = True
        except Exception as e:
            print("Error : "+str(e.args))
            self.connection.close()
        return exito


    def updateUser(self):
        id_user = self.getId()
        nombre = self.getNombre()
        telefono = self.getTelefono()
        email = self.getEmail()
        docente = self.getDocente()
        sql = "UPDATE `usuario` SET `nombre`='{}',`telefono`='{}',`email`='{}',`docente`={} WHERE `id_usuario`={}".format(nombre,telefono,email,docente,id_user)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error : "+str(e.args))
            self.connection.close()
            return False
        

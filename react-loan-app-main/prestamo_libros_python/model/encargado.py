from base import DataBase

class Encargado(DataBase):
    from base import DataBase

class Encargado(DataBase):
    
    def __init__(self, id_encargado=0, nombre_usuario="", rut="", password="") -> None:
        super().__init__()
        self.__id_encargado = id_encargado
        self.__nombre_usuario = nombre_usuario
        self.__rut = rut
        self.__password = password
    
    # Getters    
    def getIdEncargado(self):
        return self.__id_encargado
    
    def getNombreUsuario(self):
        return self.__nombre_usuario
    
    def getRut(self):
        return self.__rut
    
    def getPassword(self): 
        return self.__password
    
    # Setters
    
    def setNombreUsuario(self, newNombreUsuario):
        self.__nombre_usuario = newNombreUsuario
        self.updateEncargado()
        return True

    def setRut(self, newRut):
        self.__rut = newRut
        self.updateEncargado()
        return True
       
    def setPassword(self, newPassword):
        self.__password = newPassword
        self.updateEncargado()
        return True      
        
    def setIdEncargado(self, newIdEncargado):
        self.__id_encargado = newIdEncargado
        self.updateEncargado()
        return True    
#####################################################################

# Funciones
    def newEncargado(self, encargado):
        nombre_usuario = encargado.getNombreUsuario()
        rut = encargado.getRut()
        password = encargado.getPassword()
        
        sql = "INSERT INTO `encargado` (`nombre_usuario`, `rut`, `password`) VALUES ('{}', '{}', '{}')".format(nombre_usuario, rut, password)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False
            
    def updateEncargado(self):
        id_encargado = self.getIdEncargado()
        nombre_usuario = self.getNombreUsuario()
        rut = self.getRut()
        password = self.getPassword()
        
        sql = "UPDATE `encargado` SET `nombre_usuario`='{}', `rut`='{}', `password`='{}' WHERE `id_encargado`={}".format(nombre_usuario, rut, password, id_encargado)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False 

    def getEncargado(self):
        data = ""
        sql = "SELECT id_encargado, nombre_usuario, rut, password FROM `encargado`;"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            encargados = []
            for value in data:
                encargado = Encargado(value[0], value[1], value[2], value[3])
                encargados.append(encargado)
            self.encargados = encargados
            return encargados
        except Exception as e:
            raise

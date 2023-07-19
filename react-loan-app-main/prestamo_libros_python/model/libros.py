from base import DataBase

class Libro(DataBase):
    def __init__(self,id=0,isbn="",titulo="",autor="",editorial="",anio="") -> None:
        super().__init__()
        self.__id=id
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__publicacion = anio

    def getId(self):
        return self.__id
    def getISBN(self):
        return self.__isbn
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getEditorial(self):
        return self.__editorial
    def getPublicacion(self):
        return self.__publicacion
    
    def set(self,new):
        self.__ = new
        self.updateLibro()
        return True
    
    def setTitulo(self,newTitulo):
        self.__titulo = newTitulo
        self.updateLibro()
        return True
    def setAutor(self,newAutor):
        self.__autor = newAutor
        self.updateLibro()
        return True
    def setEditorial(self,newEditorial):
        self.__editorial = newEditorial
        self.updateLibro()
        return True
    def setPublicacion(self,newPublicacion):
        self.__publicacion = newPublicacion
        self.updateLibro()
        return True
    
    def newLibro(self,libro):
        isbn = libro.getISBN()
        titulo = libro.getTitulo()
        autor = libro.getAutor()
        editorial = libro.getEditorial()
        publicacion = libro.getPublicacion()

        sql = "INSERT INTO `libro`(`titulo`, `autor`, `editorial`, `anio_publicacion`) VALUES ('{}','{}','{}',{})".format(titulo,autor,editorial,publicacion)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            exito = True
        except Exception as e:
            print("Error : "+str(e.args))
            self.connection.close()
        return exito
    
    def updateLibro(self):
        id_libro = self.getId()
        titulo = self.getTitulo()
        autor = self.getAutor()
        editorial = self.getEditorial()
        publicacion = self.getPublicacion()

        sql = "UPDATE `libro` SET `titulo`='{}',`autor`='{}',`editorial`='{}',`anio_publicacion`='{}' WHERE `id_libro`={}".format(titulo,autor,editorial,publicacion,id_libro)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error : "+str(e.args))
            self.connection.close()
            return False


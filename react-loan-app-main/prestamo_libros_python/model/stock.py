from base import DataBase

class Stock(DataBase):
  from base import DataBase

class Stock(DataBase):
    
    def __init__(self, ISBN="", cantidad=0) -> None:
        super().__init__()
        self.__ISBN = ISBN
        self.__cantidad = cantidad
    
    # Getters    
    def getISBN(self):
        return self.__ISBN
    
    def getCantidad(self):
        return self.__cantidad
    
    # Setters
    def setISBN(self, newISBN):
        self.__ISBN = newISBN
        self.updateISBN()
        return True
    
    def setCantidad(self, newCantidad):
        self.__cantidad = newCantidad
        self.updateCantidad()
        return True

########################################################

    def getStock(self):
        data = ""
        sql = "SELECT ISBN, cantidad FROM `stock`;"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            stock_items = []
            for value in data:
                stock_item = Stock(value[0], value[1])
                stock_items.append(stock_item)
            self.stock_items = stock_items
            return stock_items
        except Exception as e:
            raise
    
    def newStock(self, stock_item):
        ISBN = stock_item.getISBN()
        cantidad = stock_item.getCantidad()
        
        sql = "INSERT INTO `stock` (`ISBN`, `cantidad`) VALUES ('{}', {})".format(ISBN, cantidad)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False
    
    def updateISBN(self):
        ISBN = self.getISBN()
        sql = "UPDATE `stock` SET `ISBN`='{}' WHERE `ISBN`='{}'".format(ISBN, ISBN)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False
    
    def updateCantidad(self):
        ISBN = self.getISBN()
        cantidad = self.getCantidad()
        sql = "UPDATE `stock` SET `cantidad`={} WHERE `ISBN`='{}'".format(cantidad, ISBN)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error: " + str(e.args))
            self.connection.close()
            return False

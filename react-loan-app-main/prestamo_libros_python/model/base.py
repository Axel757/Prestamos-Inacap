import pymysql

class DataBase:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='prestamo_libro'
        )
        try:
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise

conexion = DataBase()

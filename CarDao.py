import mysql.connector
import dbconfig as cfg

class CarDAO:
    def get_connection(self):
        return mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def create(self, car):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO cars (reg, model, price) VALUES (%s, %s, %s)"
        values = (car['Reg'], car['Model'], car['Price'])
        cursor.execute(sql, values)
        connection.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        connection.close()
        return lastrowid

    def getAll(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return [self.convertToDictionary(result) for result in results]

    def findByID(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM cars WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return self.convertToDictionary(result) if result else None

    def update(self, id, car):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE cars SET reg = %s, model = %s, price = %s WHERE id = %s"
        values = (car['Reg'], car['Model'], car['Price'], id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM cars WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()

    def convertToDictionary(self, result):
        colnames = ['id', 'Reg', 'Model', 'Price']
        car = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return car

CarDao = CarDAO()

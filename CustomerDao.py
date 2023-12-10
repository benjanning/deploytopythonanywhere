import mysql.connector
import dbconfig as cfg

class CustomerDAO:
    def get_connection(self):
        return mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def create(self, customer):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO customer (reg, name, price) VALUES (%s, %s, %s)"
        values = (customer['Reg'], customer['Name'], customer['Price'])
        cursor.execute(sql, values)
        connection.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        connection.close()
        return lastrowid

    def getAll(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM customer"
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return [self.convertToDictionary(result) for result in results]

    def findByID(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM customer WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return self.convertToDictionary(result) if result else None

    def update(self, id, customer):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE customer SET reg = %s, name = %s, price = %s WHERE id = %s"
        values = (customer['Reg'], customer['Name'], customer['Price'], id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM customer WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()

    def convertToDictionary(self, result):
        colnames = ['id', 'Reg', 'Name', 'Price']
        customer = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return customer

CustomerDao = CustomerDAO()

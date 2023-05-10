import mysql.connector

class Employe:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yasmina1501@",
            database="employes"
        )
        self.cursor = self.cnx.cursor()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def read(self):
        query = "SELECT * FROM employes"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, id_employe, nom=None, prenom=None, salaire=None,id_service=None):
        query = "UPDATE employes SET "
        values = []
        if nom is not None:
            query += "nom=%s,"
            values.append(nom)
        if prenom is not None:
            query += "prenom=%s,"
            values.append(prenom)
        if salaire is not None:
            query += "salaire=%s,"
            values.append(salaire)
        if id_service is not None:
            query += "id_service=%s,"
            values.append(id_service)
        query = query.rstrip(",")
        query += " WHERE id=%s"
        values.append(id_employe)
        self.cursor.execute(query,tuple(values))
        self.cnx.commit()

    def delete(self,id_employe):
        query = "DELETE FROM employes WHERE id=%s"
        values = (id_employe,)
        self.cursor.execute(query,values)
        self.cnx.commit()

    def close(self):
        self.cursor.close()
        self.cnx.close()

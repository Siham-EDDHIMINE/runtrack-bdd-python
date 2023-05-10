import mysql.connector

# Connexion à la base de données
cnx = mysql.connector.connect(
    host="siham",
    user="root",
    password="Yasmina1501@",
    database="databaseLaPlateforme"
)

# Création d'un curseur
cursor = cnx.cursor()

# Exécution d'une requête SQL pour calculer la capacité totale de toutes les salles
query = "SELECT SUM(capacite) FROM salles"
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchone()
capacite_totale = result[0]

# Affichage du résultat en console
print(f"La capacité totale des salles est de {capacite_totale}")

# Fermeture du curseur et de la connexion
cursor.close()
cnx.close()

import mysql.connector

# Connexion à la base de données
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yasmina1501@",
    database="databaseLaPlateforme"
)

# Création d'un curseur
cursor = cnx.cursor()

# Exécution d'une requête SQL pour calculer la superficie totale de tous les étages
query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchone()
superficie_totale = result[0]

# Affichage du résultat en console
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermeture du curseur et de la connexion
cursor.close()
cnx.close()
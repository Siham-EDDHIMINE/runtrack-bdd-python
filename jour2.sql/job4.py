import mysql.connector


# Connexion à la base de données
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yasmina1501@",
    database="databaselaplateforme"
)

# Création d'un curseur
cursor = cnx.cursor()

# Exécution d'une requête SQL pour récupérer tous les noms et capacités de la table salles
query = "SELECT nom, capacite FROM salles"
cursor.execute(query)

# Récupération des résultats
results = cursor.fetchall()

# Affichage des résultats en console
for row in results:
    nom, capacite = row
    print(f"Nom: {nom}, Capacité: {capacite}")

# Fermeture du curseur et de la connexion
cursor.close()
cnx.close()

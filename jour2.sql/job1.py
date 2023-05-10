import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yasmina1501@",
    database="databaseLaPlateforme"
)

# Création d'un curseur
cursor = db.cursor()

# Exécution d'une requête SQL pour récupérer tous les étudiants
query = "SELECT * FROM etudiants"
cursor.execute(query)

# Récupération des résultats
results = cursor.fetchall()

# Affichage des résultats en console
for line in results:
    print(line)

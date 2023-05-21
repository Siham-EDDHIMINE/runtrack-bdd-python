import mysql.connector

# Se connecter au serveur MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yasmina1501@"
)


-- Créer la table "categorie"
CREATE TABLE categorie (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nom VARCHAR(255) NOT NULL
);

-- Créer la table "produit"
CREATE TABLE produit (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nom VARCHAR(255) NOT NULL,
 prix FLOAT NOT NULL,
 quantite INT NOT NULL,
 categorie_id INT,
 FOREIGN KEY (categorie_id) REFERENCES categorie(id)
);

-- Insérer des catégories dans la table "categorie"
INSERT INTO categorie (nom) VALUES ('Electronics'), ('Clothing'), ('Home & Garden');

-- Insérer des produits dans la table "produit"
INSERT INTO produit (nom, prix, quantite, categorie_id) VALUES
('Laptop', 999.99, 10, 1),
('T-shirt', 19.99, 50, 2),
('Sofa', 399.99, 5, 3);


# Valider les modifications et fermer le curseur et la connexion
conn.commit()
cursor.close()
conn.close()

# Fermer le curseur et la connexion
cursor.close()
conn.close()



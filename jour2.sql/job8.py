import sqlite3

conn = sqlite3.connect('zoo.db')
c = conn.cursor()

# Création des tables
c.execute('''CREATE TABLE IF NOT EXISTS animal
             (id INTEGER PRIMARY KEY,
              nom TEXT,
              race TEXT,
              id_cage INTEGER,
              date_naissance TEXT,
              pays_origine TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS cage
             (id INTEGER PRIMARY KEY,
              superficie REAL,
              capacite_max INTEGER)''')

# Fonctions pour ajouter, supprimer et modifier des animaux et des cages
def ajouter_animal(id, nom, race, id_cage, date_naissance, pays_origine):
    c.execute("INSERT INTO animal VALUES (?, ?, ?, ?, ?, ?)", (id, nom, race, id_cage, date_naissance, pays_origine))
    conn.commit()

def supprimer_animal(id):
    c.execute("DELETE FROM animal WHERE id=?", (id,))
    conn.commit()

def modifier_animal(id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
    if nom:
        c.execute("UPDATE animal SET nom=? WHERE id=?", (nom,id))
    if race:
        c.execute("UPDATE animal SET race=? WHERE id=?", (race,id))
    if id_cage:
        c.execute("UPDATE animal SET id_cage=? WHERE id=?", (id_cage,id))
    if date_naissance:
        c.execute("UPDATE animal SET date_naissance=? WHERE id=?", (date_naissance,id))
    if pays_origine:
        c.execute("UPDATE animal SET pays_origine=? WHERE id=?", (pays_origine,id))
    conn.commit()

def ajouter_cage(id, superficie, capacite_max):
    c.execute("INSERT INTO cage VALUES (?, ?, ?)", (id, superficie, capacite_max))
    conn.commit()

def supprimer_cage(id):
    c.execute("DELETE FROM cage WHERE id=?", (id,))
    conn.commit()

def modifier_cage(id, superficie=None, capacite_max=None):
    if superficie:
        c.execute("UPDATE cage SET superficie=? WHERE id=?", (superficie,id))
    if capacite_max:
        c.execute("UPDATE cage SET capacite_max=? WHERE id=?", (capacite_max,id))
    conn.commit()

# Fonction pour afficher tous les animaux du zoo
def afficher_animaux():
    for row in c.execute('SELECT * FROM animal'):
        print(row)

# Fonction pour afficher la liste des animaux dans chaque cage
def afficher_animaux_par_cage():
    for row in c.execute('SELECT * FROM cage'):
        print(f"Cage {row[0]}:")
        for animal in c.execute('SELECT * FROM animal WHERE id_cage=?', (row[0],)):
            print(f"  {animal[1]}")

# Fonction pour calculer la superficie totale de toutes les cages
def calculer_superficie_totale():
    total = 0
    for row in c.execute('SELECT superficie FROM cage'):
        total += row[0]
    return total

# Exemple d'utilisation des fonctions
ajouter_animal(1, 'Simba', 'Lion', 1, '01/01/2020', 'Afrique')
ajouter_animal(2, 'Nala', 'Lionne', 1, '01/02/2020', 'Afrique')
ajouter_animal(3, 'Zazu', 'Oiseau', 2, '01/03/2020', 'Afrique')
ajouter_cage(1, 100.5, 2)
ajouter_cage(2, 50.3, 1)

print("Animaux du zoo:")
afficher_animaux()
print("\nAnimaux par cage:")
afficher_animaux_par_cage()
print(f"\nSuperficie totale: {calculer_superficie_totale()}")

conn.close()


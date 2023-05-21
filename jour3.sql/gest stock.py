import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestion des stocks")

# Créer une liste de produits
products_list = tk.Listbox(root)
products_list.insert(1, "Laptop")
products_list.insert(2, "T-shirt")
products_list.insert(3, "Sofa")
products_list.pack()

# Lancer l'application
root.mainloop()

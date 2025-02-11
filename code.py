import tkinter as tk
from tkinter import messagebox

# Code PIN de référence
PIN_CORRECT = "6931"

def saisie():
    """Récupère le PIN saisi et lance les vérifications."""
    chaine1 = entry_pin.get()
    verifier4caractere(chaine1)

def comparer2chaine(chaine1):
    """ Compare le PIN saisi avec le PIN correct """
    if chaine1 == PIN_CORRECT:
        messagebox.showinfo("Succès", "CORRECT")
    else:
        messagebox.showerror("Erreur", "INCORRECT")
        entry_pin.delete(0, tk.END)  # Efface la saisie pour réessayer

def verifier4caractere(chaine1):
    """ Vérifie si le PIN contient exactement 4 caractères """
    if len(chaine1) == 4:
        caractere_numerique(chaine1)
    else:
        messagebox.showerror("Erreur", "Entrez 4 chiffres SVP")
        entry_pin.delete(0, tk.END)

def caractere_numerique(chaine1):
    """ Vérifie si le PIN contient uniquement des chiffres """
    if chaine1.isdigit():
        comparer2chaine(chaine1)
    else:
        messagebox.showerror("Erreur", "Seulement des chiffres SVP")
        entry_pin.delete(0, tk.END)

# Interface Graphique
root = tk.Tk()
root.title("Saisie du PIN")

label = tk.Label(root, text="Entrez un code PIN à 4 chiffres :")
label.pack(pady=5)

entry_pin = tk.Entry(root, show="*", justify="center")
entry_pin.pack(pady=5)

btn_valider = tk.Button(root, text="Valider", command=saisie)
btn_valider.pack(pady=5)

root.mainloop()
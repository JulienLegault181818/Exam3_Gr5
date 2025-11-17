import hashlib

"""
On veut que notre code lise messages_gr5 et qu'il trouve que le premier message n'est pas bien hashé (mauvaise signture)

Fonction 1: lit les "messages" et découpe les mots comme dans la "signature"(sauf pour la première qui n'est pas bonne.)
Fonction 2: elle compare les "signatures" a ceux que la fonction 1 a créé.
Si les "signatures" sont pareilles print le messages valide.
Si les "signatures" ne sont pas pareilles on print le message invalide
"""

#fonction qui fait le hashing pour que la deuxième fonction puisse faire les comparaisons.

def hashing():

#fonction qui compare les deux "signatures"

def comparer():




messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}


print("Messages avec signatures validées: " )
print("Messages altérés, signtures non valide: " )

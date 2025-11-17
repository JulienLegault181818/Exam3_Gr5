import datetime
import locale
import pytest
locale.setlocale(locale.LC_TIME,'')

def afficher_jours_examens(horaire_examen: dict) -> list[str]:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """
    for i in range(len(horaire_examen)):
        jours = []
        date = datetime.datetime.strptime(horaire_examen[i], "%Y-%B-%d")#le mois n'est pas la bonne lettre m est pour minutes
        j = date.strftime("%A")# en majuscule pour donner le jour au complet et pas l'abréviation
        jours.append(j)
        return jours

if __name__ == '__main__':
    horaire_examen = {
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))

"""
# -----------------------------
# Tests unitaires
# -----------------------------
#Les tests sont inspiré de l'exercice autobus que j'ai fait à l'aide de ChatGPT.
def test_format_date():
    t = parse_time_input('10/11/2017')
    assert t.day == 10 and t.month == 11 and t.year ==2017

def test_format_invalide():
    try:
        parse_time_input('10112017')
        raised = False
    except ValueError:
        raised = True
    assert raised

def test_jour_semaine():
    t = parse_time_input('17/11/2025')
    assert t.A == lundi

def test_mauvaise_date():
    try:
        t = parse_time_input('31/02/2025')
        raised = False
    except 
    #Je ne suis pas certain de l'exption d'une date qui n'existe pas.
    
    
    """

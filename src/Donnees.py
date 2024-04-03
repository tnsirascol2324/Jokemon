from Creatures import *
from Personnage import *
from Actions_Creatures import *
from copy import deepcopy

### Dictionnaires d'Actions_Creatures, liste des actions avec les caractéristiques propres à chacune
dict_Actions_Creatures = {
    "Lame Tranchante" : Action_Creature("Lame Tranchante", Type_Action.ATTAQUE, 10, Element.AIR)
}

### Dictionnaire de Creature, liste des creatures avec les caractéristiques propres à chacun
dict_Creatures = {
    "Salameche" : Creature("Salameche", 30, Element.FEU, [dict_Actions_Creatures["Lame Tranchante"]]),
    "Picachute du Niagara" : Creature("Picachute du Niagara", 100, Element.EAU, []),
    "Carapax" : Creature("Carapax", 70, Element.TERRE, []),
    "Magicorvée" : Creature("Magicorvée", 90, Element.EAU, []),
    "Dracofeur" : Creature("Dracofeur", 100, Element.FEU, [])
}

### Dictionnaires de Personnage
dict_Personnage = {
    "Michel" : Personnage("Michel", 10, Rang.Entraineur, [dict_Creatures["Carapax"]])
}

## Fonction pour obtenir une copie d'un objet avec les mêmes caractéristiques de l'original
def cloner(liste_choisie : dict, objet : str) :
    '''Renvoie une pure copie de ce qu'on l'on depuis le dictionnaire voulu'''
    return deepcopy(liste_choisie[objet])


# Tests
if __name__ == "__main__" :
    michel = cloner(dict_Personnage, "Michel")
    dict_Creatures["Carapax"].surnom = "Truc"
    # michel.ajouter_Creature(cloner(dict_Creatures, "Carapax"))
    # michel.ajouter_Creature(cloner(dict_Creatures, "Magicorvée"))
    print(michel)
    print(dict_Personnage["Michel"])
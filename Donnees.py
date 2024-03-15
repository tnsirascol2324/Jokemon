from Creatures import *
from Actions_Creatures import *
from copy import deepcopy

### Dictionnaire de Creature, liste des creatures avec les caractéristiques propres à chacun
liste_Creatures = {
    "Salameche" : Creature("Salameche", 30, Elements.FEU, []),
    "Picachute du Niagara" : Creature("Picachute du Niagara", 100, Elements.EAU, []),
    "Carapax" : Creature("Carapax", 70, Elements.EAU, []),
    "Magicorvée" : Creature("Magicorvée", 90, Elements.EAU, []),
    "Dracofeur" : Creature("Dracofeur", 100, Elements.FEU, [])
}

### Dictionnaires d'Actions_Creatures, liste des actions avec les caractéristiques propres à chacune
liste_Actions_Creatures = {
    "Lame Tranchante" : Action_Creature("Lame Tranchante", Type_Action.ATTAQUE, 10, Elements.AIR)
}

## Fonction pour obtenir une copie d'un objet avec les mêmes caractéristiques de l'original
def cloner(liste_choisie : dict, nom_Espece : str) :
    return deepcopy(liste_choisie[nom_Espece])

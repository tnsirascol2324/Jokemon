# class Joueur :
#     def __init__(self, param_Pv) :
#         pv = param_Pv
#         inventaire = Inventaire()
#         sprite = None

# class Inventaire :
#     def __init__(self) :
#         creatures = []
#         objets = []



class Creature :

    def __init__(self, param_Surnom = "Placeholder", param_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Attaques = [], param_Element = None) :
        surnom = param_Surnom
        pv = param_Pv
        nom_Espece = param_Nom_Espece
        liste_Attaques = param_Liste_Attaques
        element = param_Element

class Creature_Feu(Creature) :
    
    def __init__(self):
        super().__init__()
        self.element = "Feu"

class Creature_Eau(Creature) :

    def __init__(self):
        super().__init__()
        self.element = "Eau"

class Creature_Terre(Creature) :

    def __init__(self):
        super().__init__()
        self.element = "Terre"

class Creature_Air(Creature) :

    def __init__(self):
        super().__init__()
        self.element = "Air"

# Exemple de création d'un type de pokemon :
class Salameche(Creature_Feu) :

    def __init__(self):
        super().__init__()
        self.pv = 30
        self.nom_Espece = "Salameche"


# class Actions_Creatures :
#     def __init__(self) :
#         nom =
#         degats =
#         type_Action =
#         element =
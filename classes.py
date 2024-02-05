### Super-classe Creature
class Creature :
    '''Super-classe Creature :
    Creer un objet :
        ma_Creature = Creature(Surnom[str], Pv[int], Nom_Espece[str], Liste_d_Actions[liste d'objet de la classe Actions_Creatures], Element[str])
    
    Attributs :
        surnom[str] | pv[int] | nom_Espece[str] | liste_Actions[list*] | element[str]
        liste_Actions : Liste d'objet de la CLasse Actions_Creatures
    
    Methodes :

    '''
    ## Initialisation
    def __init__(self, param_Surnom = "Placeholder", param_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = [], param_Element = None) :
        surnom = param_Surnom
        pv = param_Pv
        nom_Espece = param_Nom_Espece
        liste_Actions = param_Liste_Actions
        element = param_Element
    
    ## Méthodes
        

### Sous-classe Feu
class Creature_Feu(Creature) :
    ## Initialisation
    def __init__(self, param_Surnom = "Placeholder", param_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = [], param_Element = None):
        Creature.__init__(self, param_Surnom, param_Pv, param_Nom_Espece, param_Liste_Actions, param_Element)
        self.element = "Feu"

### Sous-classe Eau
class Creature_Eau(Creature) :
    ## Initialisation
    def __init__(self, param_Surnom = "Placeholder", param_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = [], param_Element = None):
        Creature.__init__(self, param_Surnom, param_Pv, param_Nom_Espece, param_Liste_Actions, param_Element)
        self.element = "Eau"

### Sous-classe Terre
class Creature_Terre(Creature) :
    ## Initialisation
    def __init__(self, param_Surnom = "Placeholder", param_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = [], param_Element = None):
        Creature.__init__(self, param_Surnom, param_Pv, param_Nom_Espece, param_Liste_Actions, param_Element)
        self.element = "Terre"

### Sous-classe Air
class Creature_Air(Creature) :
    ## Initialisation
    def __init__(self, param_Surnom = "Placeholder", param_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = [], param_Element = None):
        Creature.__init__(self, param_Surnom, param_Pv, param_Nom_Espece, param_Liste_Actions, param_Element)
        self.element = "Air"

# Exemple de création d'un type de pokemon :
class Salameche(Creature_Feu) :

    def __init__(self):
        Creature.__init__(self)
        self.pv = 30
        self.nom_Espece = "Salameche"


# class Actions_Creatures :
#     def __init__(self) :
#         nom =
#         degats =
#         type_Action =
#         element =
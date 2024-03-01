from typing import Self
from Actions_Creatures import *

### Super-classe Creature
class Creature :
    '''# Super-classe Creature :
    Creer un objet :
        ma_Creature = Creature(Max_Pv[int], Nom_Espece[str], Liste_d_Actions[liste d'objet de la classe Actions_Creatures], Element[Membre de Elements])
    
    Attributs :
        surnom[str] | _max_Pv[int] | _pv[int] | _nom_Espece[str] | _liste_Actions[list*] | _element[Elements._____]
        _liste_Actions : Liste d'objet de la Classe Actions_Creatures
        _element : Membre de l'Enum Elements (voir Actions_Creatures.py)
    
    Methodes :
    - get_max_Pv() -> Explicite
    - get_Pv() -> Explicite
    - get_nom_Espece() -> Explicite
    - get liste_Actions() -> Explicite
    - get_element() -> Explicite
    - changer_Surnom(nom) -> change le surnom avec "nom"
    - prendre_Degats(nbr) -> enlève "nbr" pv à la créature, pv minimum à 0
    - soigner_Pv(nbr) -> ajoute "nbr" pv à la créature, pv maximum à "
    - executer_Action(action, cible) -> soigne ou attaque la "cible" en fonction de l "action" utilisé (action : Actions_Creatures() | cible : Creature())
    '''
    def __init__(self, param_Max_Pv = 20, param_Nom_Espece = "Null", param_Liste_Actions = [], param_Element = None) :
        self.surnom = param_Nom_Espece + " sauvage"
        self._max_Pv = param_Max_Pv
        self._pv = param_Max_Pv
        self._nom_Espece = param_Nom_Espece
        self._liste_Actions = param_Liste_Actions
        self._element = param_Element
    
    def __str__(self) :
        return f"Fiche recap de {self.surnom} :\n- Pv : {self._pv}/{self._max_Pv}\n- Espece : {self._nom_Espece}\n- Element : {self._element}\n- Actions : {', '.join([action._nom for action in self._liste_Actions])}"

    ## Accesseurs
    def get_max_Pv(self) :
        return self._max_Pv

    def get_Pv(self) :
        return self._pv

    def get_nom_Espece(self) :
        return self._nom_Espece
    
    def get_liste_Actions(self) :
        return self._liste_Actions
    
    def get_element(self) :
        return self._element
    
    ## Mutateurs
    def changer_Surnom(self, nouveau_Surnom) :
        self.surnom = nouveau_Surnom

    def prendre_Degats(self, degats) :
        self._pv = self._pv - degats
        if self._pv < 0 :
            self._pv = 0
    
    def soigner_Pv(self, soin) :
        self._pv += soin
        if self._pv > self._max_Pv :
            self._pv = self._max_Pv
    
    def executer_Action(self, action : Actions_Creatures, cible : Self) :
        type_Action = action.get_type_Action()
        if type_Action == Type_Action.SOIN :
            cible.soigner_Pv(action.get_puissance())
        elif type_Action == Type_Action.ATTAQUE :
            cible.prendre_Degats(action.get_puissance())

### Sous-classe Feu
class Creature_Feu(Creature) :
    def __init__(self, param_Surnom = "Placeholder", param_Max_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = []):
        Creature.__init__(self, param_Surnom, param_Max_Pv, param_Nom_Espece, param_Liste_Actions)
        self._element = "Feu"

### Sous-classe Eau
class Creature_Eau(Creature) :
    def __init__(self, param_Surnom = "Placeholder", param_Max_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = []):
        Creature.__init__(self, param_Surnom, param_Max_Pv, param_Nom_Espece, param_Liste_Actions)
        self._element = "Eau"

### Sous-classe Terre
class Creature_Terre(Creature) :
    def __init__(self, param_Surnom = "Placeholder", param_Max_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = []):
        Creature.__init__(self, param_Surnom, param_Max_Pv, param_Nom_Espece, param_Liste_Actions)
        self._element = "Terre"

### Sous-classe Air
class Creature_Air(Creature) :
    def __init__(self, param_Surnom = "Placeholder", param_Max_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = []):
        Creature.__init__(self, param_Surnom, param_Max_Pv, param_Nom_Espece, param_Liste_Actions)
        self._element = "Air"


# Exemples
attaque = Actions_Creatures("Lame Tranchante", 30, Type_Action.ATTAQUE, Elements.AIR)
attaque1 = Actions_Creatures("Mini potion", 10, Type_Action.SOIN, Elements.EAU)
salameche = Creature_Feu(35, "Salameche", [attaque, attaque1])

print(salameche, "\n")
print(attaque, attaque1, sep="\n\n")
print(list(map(lambda x:x.get_nom(),salameche.get_liste_Actions())))
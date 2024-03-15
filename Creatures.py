from typing import Self
from Actions_Creatures import *
from Etres_Vivants import *

### Super-classe Creature
class Creature(Etre_Vivant) :
    '''# Classe Creature :
    Classe fille de la classe Etre_Vivant

    Creer un objet :
        ma_Creature = Creature(Nom_Espece[str], Max_Pv[int], Element[Membre de Elements], Liste_d_Actions[liste d'objet de la classe Actions_Creatures])
        
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
    def __init__(self, param_Nom_Espece = "Null", param_Max_Pv = 20, param_Element = Elements.NULL, param_Liste_Actions = []) :
        Etre_Vivant.__init__(self, param_Max_Pv, param_Nom_Espece + " sauvage")
        self._nom_Espece = param_Nom_Espece
        self._liste_Actions = param_Liste_Actions
        self._element = param_Element
    
    def __str__(self) :
        return f"Fiche recap de {self.surnom} :\n- Pv : {self._pv}/{self._max_Pv}\n- Espece : {self._nom_Espece}\n- Element : {self._element}\n- Actions : {', '.join([action._nom for action in self._liste_Actions])}"

    ## Accesseurs
    def get_nom_Espece(self) :
        return self._nom_Espece
    
    def get_liste_Actions(self) :
        return self._liste_Actions
    
    def get_element(self) :
        return self._element
    
    ## Mutateurs  
    def executer_Action(self, action : Action_Creature, cible : Self) :
        type_Action = action.get_type_Action()
        if type_Action == Type_Action.SOIN :
            cible.soigner_Pv(action.get_puissance())
        elif type_Action == Type_Action.ATTAQUE :
            cible.prendre_Degats(action.get_puissance())
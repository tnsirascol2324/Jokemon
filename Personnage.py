from Creatures import *
from Etres_Vivants import *
from enum import IntEnum, auto

## IntEnum Rangs
class Rang (IntEnum) :
    Null = -1
    Joueur = 0
    Entraineur = auto()
    Boss = auto()

### Super-classe Creature
class Personnage(Etre_Vivant) :
    '''# Classe Personnage :
    Classe fille de la classe Etre_Vivant !!

    Creer un objet :
        mon_Perso = Personnage(Max_Pv[int], Surnom[str], Rang[Membre de Rang], Inventaire_Creatures[liste d'objet de la classe Creature])
        
    Attributs :
        _max_Pv[int] | surnom[str] | _rang[Rang._____] | _inventaire_Creatures[list*]
        _inventaire_Creatures : Liste d'objet de la Classe Creatures
    
    Methodes :
    - get_rang() -> Renvoie l attribut _rang de l objet
    - get_inventaire_Creatures() -> Renvoie l attribut _inventaire_Creatures de l objet
    - ajouter_Creature(creature) -> Ajoute une Creature à l inventaire du personnage 
    '''
    def __init__(self, param_Surnom : str = "Null", param_Max_Pv : int = 20, param_Rang : Rang = Rang.Null, param_inventaire_Creatures : list[Creature] = []) :
        Etre_Vivant.__init__(self, param_Max_Pv, param_Surnom)
        self._rang = param_Rang
        self._inventaire_Creatures = param_inventaire_Creatures
        self._inventaire_Objets = None
    
    def __str__(self) -> str :
        '''Renvoie une fiche recap de l objet'''
        return f"Fiche recap de {self.surnom} :\n- Pv : {self._pv}/{self._max_Pv}\n- Rang : {self._rang.name}\n- Inventaire : {', '.join([creature.surnom for creature in self._inventaire_Creatures])}"
    
    ## Accesseurs
    def get_rang(self) -> Rang :
        '''Renvoie l attribut _rang de l objet'''
        return self._rang
    
    def get_inventaire_Creatures(self) -> list[Creature] :
        '''Renvoie l attribut _inventaire_Creatures de l objet'''
        return self._inventaire_Creatures
    
    ## Mutateurs
    def ajouter_Creature(self, creature : Creature) :
        '''Ajoute une Creature à l inventaire du personnage'''
        self._inventaire_Creatures.append(creature)
from enum import StrEnum

### Enums Type_Action et Elements
class Element(StrEnum) :
    NULL = "Null"
    FEU = "Feu"
    EAU = "Eau"
    TERRE = "Terre"
    AIR = "Air"

class Type_Action(StrEnum) :
    NULL = "Null"
    SOIN = "Soin"
    ATTAQUE = "Attaque"

### Super-classe Actions_Creatures
class Action_Creature :
    '''# Classe Actions_Creatures :
    Creer un objet :
        mon_Action = Creature(Nom[str], Type_de_l_Actions[Membre de Type_Action], Puissance_de_l_Action[int], Element[Membre de Elements])
    
    Attributs :
        _nom[str] | _type_Action[Type_Action._____] | _puissance[int] | _element[Elements.______]
        _type_Action : membre de l'Enum Type_Action
        _element : membre de l'Enum Elements
    
    Methodes :
    - get_nom() -> Renvoie l'attribut _nom de l'objet
    - get_type_Action() -> Renvoie l'attribut _type_Action de l'objet
    - get_puissance() -> Renvoie l'attribut _puissance de l'objet
    - get_element() -> Renvoie l'attribut _element de l'objet
    '''
    def __init__(self, param_Nom : str = "Null", param_Type_action : Type_Action = Type_Action.NULL, param_Puissance : int = 5, param_Element : Element = Element.NULL) :
        self._nom = param_Nom
        self._puissance = param_Puissance
        self._type_Action = param_Type_action
        self._element = param_Element

    def __str__(self) :
        '''Renvoie une fiche recap de l'action, affichant tous ses attributs de manière COOL ! B]'''
        return f"Fiche recap de {self._nom} :\n- {self._type_Action} : {self._puissance}\n- Element : {self._element}"
    
    ## Accesseurs
    def get_nom(self) -> str :
        '''Renvoie l'attribut _nom de l'objet'''
        return self._nom
        
    def get_type_Action(self) -> Type_Action :
        '''Renvoie l'attribut _type_Action de l'objet'''
        return self._type_Action
    
    def get_puissance(self) -> int :
        '''Renvoie l'attribut _puissance de l'objet'''
        return self._puissance
    
    def get_element(self) -> Element :
        '''Renvoie l'attribut _element de l'objet'''
        return self._element
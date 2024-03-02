from enum import StrEnum

### Enums Type_Action et Elements
class Elements(StrEnum) :
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
class Actions_Creatures :
    '''# Super-classe Actions_Creatures :
    Creer un objet :
        mon_Action = Creature(Nom[str], Type_de_l_Actions[Membre de Type_Action], Puissance_de_l_Action[int], Element[Membre de Elements])
    
    Attributs :
        _nom[str] | _type_Action[Type_Action._____] | _puissance[int] | _element[Elements.______]
        _type_Action : membre de l'Enum Type_Action
        _element : membre de l'Enum Elements
    
    Methodes :
    - get_nom() -> Explicite
    - get_type_Action() -> Explicite
    - get_puissance() -> Explicite
    - get_element() -> Explicite
    '''
    def __init__(self, param_Nom = "Null", param_Type_action = Type_Action.NULL, param_Puissance = 1, param_Element = Elements.NULL) :
        self._nom = param_Nom
        self._puissance = param_Puissance
        self._type_Action = param_Type_action
        self._element = param_Element

    def __str__(self) :
        return f"Fiche recap de {self._nom} :\n- {self._type_Action} : {self._puissance}\n- Element : {self._element}"
    
    ## Accesseurs
    def get_nom(self) :
        return self._nom
        
    def get_type_Action(self) :
        return self._type_Action
    
    def get_puissance(self) :
        return self._puissance
    
    def get_element(self) :
        return self._element
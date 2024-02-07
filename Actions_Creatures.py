### Super-classe Actions_Creatures
class Actions_Creatures :
    '''# Super-classe Actions_Creatures :
    Creer un objet :
        mon_Action = Creature(Nom[str], Puissance_de_l_Action[int], Type_de_l_Actions[int (O ou 1)], Element[str])
    
    Attributs :
        _nom[str] | _puissance[int] | _type_Action[int*] | _element[str]
        type_Action : 1 (Attaque) ou 0 (Soin)
    
    Methodes :
    - get_nom() -> Explicite
    - get_puissance() -> Explicite
    - get_type_Action() -> Explicite
    - get_element() -> Explicite
    '''
    def __init__(self, param_Nom = "Placeholder", param_Puissance = 1, param_Type_action = 1, param_Element = None) :
        self._nom = param_Nom
        self._puissance = param_Puissance
        self._type_Action = param_Type_action
        self._element = param_Element

    def __str__(self) :
            if self._type_Action == 1 :
                return f"Fiche recap de {self._nom} :\n- Attaque : {self._puissance} degats\n- Element : {self._element}"
            elif self._type_Action == 0 :
                return f"Fiche recap de {self._nom} :\n- Soins : {self._puissance} pvs\n- Element : {self._element}"
    
    ## Accesseurs
    def get_nom (self) :
        return self._nom
    
    def get_puissance (self) :
        return self._puissance
    
    def get_type_Action (self) :
        return self._type_Action
    
    def get_element(self) :
        return self._element
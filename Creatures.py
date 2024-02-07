import Actions_Creatures

### Super-classe Creature
class Creature :
    '''# Super-classe Creature :
    Creer un objet :
        ma_Creature = Creature(Surnom[str], Pv[int], Nom_Espece[str], Liste_d_Actions[liste d'objet de la classe Actions_Creatures], Element[str])
    
    Attributs :
        surnom[str] | _max_Pv[int] | _pv[int] | _nom_Espece[str] | _liste_Actions[list*] | _element[str]
        liste_Actions : Liste d'objet de la CLasse Actions_Creatures
    
    Methodes :
    - get_max_Pv() -> Explicite
    - get_Pv() -> Explicite
    - get_nom_Espece() -> Explicite
    - get liste_Actions() -> Explicite
    - get_element() -> Explicite
    - prendre_Degats(nbr) -> enlève "nbr" pv à la créature, pv minimum à 0
    - soigner_Pv(nbr) -> ajoute "nbr" pv à la créature, pv maximum à "
    - executer_Action(action, cible) -> soigne ou attaque la "cible" en fonction de l "action" utilisé (action : Actions_Creatures() | cible : Creature())
    '''
    def __init__(self, param_Surnom = "Placeholder", param_Max_Pv = 20, param_Nom_Espece = "Placeholder", param_Liste_Actions = [], param_Element = None) :
        self.surnom = param_Surnom
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
    def prendre_Degats(self, degats) :
        self._pv = self._pv - degats
        if self._pv < 0 :
            self._pv = 0
    
    def soigner_Pv(self, soin) :
        self._pv += soin
        if self._pv > self._max_Pv :
            self._pv = self._max_Pv
    
    def executer_Action(self, action, cible) :
        type_Action = action._get_type_Action()
        if type_Action == 0 :
            cible.soigner_Pv(action.get_puissance())
        elif type_Action == 1 :
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
attaque = Actions_Creatures("Lame Tranchante", 30, 1, "Feu")
attaque1 = Actions_Creatures("Mini potion", 10, 0, "Eau")
salameche = Creature_Feu("Michel", 35, "Salameche", [attaque, attaque1])

print(salameche, "\n")
print(attaque, attaque1, sep="\n\n")
print(list(map(lambda x:x.get_nom(),salameche.get_liste_Actions())))
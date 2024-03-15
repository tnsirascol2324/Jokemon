### Super-classe Etre_Vivant
class Etre_Vivant :
    '''# Super-classe Etre_Vivant :
    Classe mère de Creature et Personnage
    
    Creer un objet :
        Truc = Etre_Vivant(Max_Pv[int], Surnom[str])
        
    Attributs :
        surnom[str] | _max_Pv[int] | _pv[int]
    
    Methodes :
    - get_max_Pv() -> Explicite
    - get_Pv() -> Explicite
    - changer_Surnom(nom) -> change le surnom avec "nom"
    - prendre_Degats(nbr) -> enlève "nbr" pv à la créature, pv minimum à 0
    - soigner_Pv(nbr) -> ajoute "nbr" pv à la créature, pv maximum à "
    '''
    def __init__(self, param_Max_Pv = 20, param_Surnom = "Null") :
        self.surnom = param_Surnom
        self._pv = param_Max_Pv
        self._max_Pv = param_Max_Pv

    def __str__(self) :
        return f"Fiche recap de {self.surnom} :\n- Pv : {self._pv}/{self._max_Pv}"

    ## Acceseurs
    def get_max_Pv(self) :
        return self._max_Pv

    def get_Pv(self) :
        return self._pv
    
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
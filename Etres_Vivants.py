### Super-classe Etre_Vivant
class Etre_Vivant :
    '''# Super-classe Etre_Vivant :
    Classe mère de Creature et Personnage
    
    Creer un objet :
        mon_Etre_Vivian = Etre_Vivant(Max_Pv[int], Surnom[str])
        
    Attributs :
        surnom[str] | _max_Pv[int] | _pv[int]
    
    Methodes :
    - get_max_Pv() -> Renvoie l attribut _max_Pv de l objet
    - get_pv() -> Renvoie l attribut _pv de l objet
    - changer_Surnom(nom) -> Change le surnom avec "nom"
    - prendre_Degats(nbr) -> Enlève "nbr" pv à la créature, pv minimum à 0
    - soigner_Pv(nbr) -> Ajoute "nbr" pv à la créature, pv maximum à "self._max_Pv"
    '''
    def __init__(self, param_Max_Pv : int = 20, param_Surnom : str = "Null") :
        self.surnom = param_Surnom
        self._pv = param_Max_Pv
        self._max_Pv = param_Max_Pv

    def __str__(self) -> str :
        '''Renvoie une fiche recap de l objet, affichant tous ses attributs'''
        return f"Fiche recap de {self.surnom} :\n- Pv : {self._pv}/{self._max_Pv}"

    ## Accesseurs
    def get_max_Pv(self) -> int :
        '''Renvoie l attribut _max_Pv de l objet'''
        return self._max_Pv

    def get_pv(self) -> int :
        '''Renvoie l attribut _pv de l objet'''
        return self._pv
    
    ## Mutateurs
    def changer_Surnom(self, nouveau_Surnom : str) :
        '''Change le surnom avec "nom" '''
        self.surnom = nouveau_Surnom
    
    def prendre_Degats(self, degats : int) :
        '''Enlève "nbr" pv à la créature, pv minimum à 0'''
        self._pv = self._pv - degats
        if self._pv < 0 :
            self._pv = 0
    
    def soigner_Pv(self, soin : int) :
        '''Ajoute "nbr" pv à la créature, pv maximum à "self._max_Pv"'''
        self._pv += soin
        if self._pv > self._max_Pv :
            self._pv = self._max_Pv
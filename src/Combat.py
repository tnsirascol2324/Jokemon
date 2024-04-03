from Creatures import *
from Actions_Creatures import *

class Combat :

    def __init__(self, param_nom, param_Max_pv, param_Listes_Actions, param_Type_action):
        self._nom = param_nom
        self._Max_pv = param_Max_pv
        self._Listes_Actions = param_Listes_Actions
        self._Type_action = param_Type_action


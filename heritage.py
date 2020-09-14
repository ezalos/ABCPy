class MaClasseMere():
    def __init__(self):
        self.thing = 1
        self.attribut_classe_mere = 'premiere valeur'

class MaClasseFille(MaClasseMere):
    def __init__(self):
	# Une fois la classe mère définie, il va vous falloir l'initialiser.
	# Pour cela, il suffit d'appeler le constructeur de la classe mère dans le constructeur de la classe fille :
        MaClasseMere.__init__(self)
        # super().__init__() est identique a la ligne au dessus, compatible 3.X uniquement, dispense de self

	# surcharge
        self.attribut_classe_mere = 'nouvelle valeur'

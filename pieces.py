#Exo 1
import random
class Piece :
    def tirage_aleatoire(self, precedent) :
        return random.randint(0,1)
    def moyenne_tirage(self, n):
        tirage = [ ]
        for i in range (n) :
            precedent = tirage[-1] if i > 0 else None
            tirage.append( self.tirage_aleatoire (precedent) )
        s = sum(tirage)
        return s * 1.0 / len(tirage)

p = Piece()
print ("Exo 1: ", p.moyenne_tirage(100))

#Exo 2
class PieceTruquee (Piece) :
    def tirage_aleatoire(self, precedent) :
        if precedent == None or precedent == 1 :
            return random.randint(0,1)
        else :
            return 1 if random.randint(0,9) >= 3 else 0

p = PieceTruquee()
print ("Exo 2: ", p.moyenne_tirage(100))



#Exo 3
class PieceTruqueeMix (PieceTruquee) :
    def tirage_aleatoire(self, precedent) :
        if random.randint(0,1) == 0 :
            return Piece.tirage_aleatoire(self, precedent)
        else :
            return PieceTruquee.tirage_aleatoire(self, precedent)

p = PieceTruqueeMix()
print ("Exo 3: ", p.moyenne_tirage(100))


#Exo 4
# ce qui vient de l'énoncé
def moyenne_tirage(n, fonction):
    """
    cette fonction fait la moyenne des résultats produits par la fonction passée en argument
    """
    tirage = [ ]
    for i in range (n) :
        precedent = tirage[-1] if i > 0 else None
        tirage.append( fonction (precedent) )
    s = sum(tirage)
    return s * 1.0 / len(tirage)

def truquee (precedent) :
    if precedent == None or precedent == 1 :
        return random.randint(0,1)
    else :
        return 1 if random.randint(0,9) >= 3 else 0

# la partie ajoutée pour la correction
lamba_fun = lambda v : random.randint(0,1) if random.randint(0,1) == 0 else truquee(v)
#print ("Exo 4: ", moyenne_tirage(100, lamda_fun))



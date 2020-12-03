from fTrie import Trie #fonction qui trie la liste de mot avec des sous liste par rapport au nombre de mots
from FgenDuMot import GenDuMot #fonction qio génère le mot donné au joueur(version caché)
from fJeux import Jouer #fonction récursive qui permet de jouer
import random
Mots = ["Docteur", "Sherlock", "Dalek", "Sensei","Jeffrey","Sherlocl", "rastacolerapados","infinity war","rastacolerapadoa"]

ListeOrdonnée=Trie(Mots)
print(ListeOrdonnée)
MotAlea=ListeOrdonnée[random.randint(0, len(ListeOrdonnée)-1)][0] #choisis un mot aléatoirement
print(MotAlea)
MotCaché=GenDuMot(MotAlea)
print(MotCaché)


jeux=Jouer(MotAlea,MotCaché,8,[])
print(jeux)






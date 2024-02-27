from classdef import *

a=Mediatheque()
livre=Livre('Les Misérables','Victor Hugo',2000,192,'Pathé')
cd =Cd('Liberté','',0,15,1)
cd2 =Cd('Liberté','Victor Hugo',0,15,1)
dvd = Dvd('Les Misérables le film','Victor Hugo',2000,198)
print(dvd)
print(livre)
print(cd)
article = Article_de_Magazine('Le bazard','Victor Hugo',1902,'Les grands savants',12,1)
a._Mediatheque__ajouter_medium(livre)
a._Mediatheque__ajouter_medium(cd)
a._Mediatheque__ajouter_medium(cd2)
a._Mediatheque__ajouter_medium(dvd)
a._Mediatheque__ajouter_medium(article)
print('test fonction 2')

a._Mediatheque__recherche_auteur('Victor Hugo')


print()
print()
print()
#x=a._Mediatheque__supprimer_medium('Les Misérables le film','Victor Hugo')
#print(x)
#a._Mediatheque__supprimer_auteur('Victor Hugo')
a._Mediatheque__recherche_auteur('Victor Hugo')

print(a._Mediatheque__pret('Julien','Les Misérables','Victor Hugo'))
print(a._Mediatheque__pret('Julien','','Victor Hugo'))
a._Mediatheque__pret('Julien','Liberté','')
print(a._Mediatheque__compte_pret())

a._Mediatheque__ajouter_input()
a._Mediatheque__recherche_auteur('Rah')
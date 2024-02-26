from abc import ABC
class Medium (ABC) :
    def __init__ (self,titre ='',auteur='',date=0) :
        self.titre = titre
        self.auteur = auteur
        self.date_parution = date
        self.nom_pret = ''

    def __ajouter_pret(self,nom :str):
        self.nom_pret = nom
class Livre (Medium):
    def __init__(self, titre='', auteur='', date=0,pages=0,editeur=''):
        super().__init__(titre, auteur, date)
        self.pages = pages
        self.editeur = editeur

    def __str__(self):
        return f'{self.titre} de {self.auteur},{self.date_parution},{self.pages} pages, {self.editeur}'

class Cd (Medium):
    def __init__(self, titre='', auteur='', date=0,duree = 0,morceaux=0):
        super().__init__(titre, auteur, date)
        self.duree = duree
        self.morceaux = morceaux

    def __str__(self):
        return f'{self.titre} de {self.auteur},{self.date_parution},{self.duree} min, {self.morceaux} morceaux'

class Dvd (Medium):
    def __init__(self, titre='', auteur='', date=0,duree = 0):
        super().__init__(titre, auteur, date)
        self.duree = duree
    def __str__(self):
        return f'{self.titre} de {self.auteur},{self.date_parution},{self.duree} min'

class Article_de_Magazine(Medium):
    def __init__(self , titre='' , auteur='' , date=0 , nom_mag = '' , numero_mag =0 , intervalle_page = 0):
        super().__init__(titre, auteur, date)
        self.nom_mag = nom_mag
        self.numero_mag = numero_mag
        self.intervalle_page = intervalle_page

    def __str__(self):
        return f'{self.titre} de {self.auteur},{self.date_parution},dans {self.nom_mag} N°{self.numero_mag} {self.intervalle_page} pages'
    

class Mediatheque(object):
    def __init__(self,list_medium=[]):
        self.list_medium = list_medium
    
    def __ajouter_medium (self,medium : Medium):
        self.list_medium.append(medium)

    def __recherche_auteur(self,auteur: str):
        for medium in self.list_medium :
            if medium.auteur == auteur :
                print(medium)
    
    def __supprimer_medium(self,titre : str,auteur:str) :
        i=0
        for medium in self.list_medium :
            if medium.auteur == auteur and medium.titre == titre :
                supp=self.list_medium.pop(i)
                print(supp,' a bien été supprimé')
                return i        #retourne l'indice où était placé l'élément
            i+=1
        print('Aucun medium de ce type dans la médiathèque')
        return -1               #éléments pas dans la médiathéque
    
    def __supprimer_auteur(self,auteur : str):
        i=0
        for medium in self.list_medium :
            if medium.auteur == auteur:
                supp=self.list_medium.pop(i)
                print(supp,' a bien été supprimé')
            i+=1
      
    def __pret(self,nom_pret : str, titre : str, auteur :str):
        for medium in self.list_medium :
            if medium.auteur == auteur and medium.titre == titre :
                medium._Medium__ajouter_pret(nom_pret)
                return 1
        print('Aucun medium de ce type dans la médiathèque')
        return 0

    def __compte_pret(self):
        res = 0
        for medium in self.list_medium :
            if medium.nom_pret != '' :
                res += 1
        return res


    
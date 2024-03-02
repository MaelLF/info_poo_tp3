from abc import ABC

#Auteur : Le Floch Mael
#Date de création : 26 Février 2024

#Objectif du programme : Création de classes permettant la simulation d'une médiathéque :
# -la création d'une classe abstraite medium possédant des classes dérivées (Livre, Cd , Dvd et Article de Magazine)
# -la gestion de cette médiathèque (ajout,suppression, affcihage et prêt)
# -l'ajout de medium à travers le terminal (input())
# -permettre l'ajout de classe dérivée de medium avec le moins de difficultés possibles



class Medium (ABC) : #Définition d'une classe abstraite Medium
    def __init__ (self,titre ='',auteur='',date=0) : #Chaque médium a un titre, un auteur et une date ainsi que le nom de la personne à qui il a été prêté
        self.titre = titre
        self.auteur = auteur
        self.date_parution = date
        self.nom_pret = ''

    def __ajouter_pret(self,nom :str): #Méthode d'ajout d'un prêt
        self.nom_pret = nom

    def __str__(self): #Méthode d'affichage d'un médium
        return f'{self.titre} de {self.auteur},{self.date_parution}' 

    def input_medium (self):    #Méthode d'ajout d'un médium par le terminal
        self.titre = input("Titre : ")
        self.auteur = input("Auteur : ")
        self.date_parution = int(input("Date : "))

class Livre (Medium): #Définition de la classe Livre dérivée de la classe Medium
    def __init__(self, titre='', auteur='', date=0,pages=0,editeur=''): #Un livre est un médium avec un nombre de pages et un éditeur
        super().__init__(titre, auteur, date)
        self.pages = pages
        self.editeur = editeur

    def __str__(self): #Méthode d'affichage d'un livre
        return f'{self.titre} de {self.auteur},{self.date_parution},{self.pages} pages, {self.editeur}' 

    def input_livre(self): #Méthode d'ajout d'un livre par le terminal
        self.input_medium()
        self.pages = int(input("Pages : "))
        self.editeur= input("Editeur : ")

class Cd (Medium): #Définition de la classe Cd dérivée de la classe Medium
    def __init__(self, titre='', auteur='', date=0,duree = 0,morceaux=0): #Un Cd est un médium avec une durée et un nombre de morceaux
        super().__init__(titre, auteur, date)
        self.duree = duree
        self.morceaux = morceaux

    def __str__(self):  #Méthode d'affichage d'un Cd
        return f'{self.titre} de {self.auteur},{self.date_parution},{self.duree} min, {self.morceaux} morceaux'
    
    def input_cd(self): #Méthode d'ajout d'un Cd par le terminal
        self.input_medium()
        self.duree = int(input("Durée : "))
        self.morceaux = int(input("Morceaux : "))

class Dvd (Medium): #Définition de la classe Dvd dérivée de la classe Medium
    def __init__(self, titre='', auteur='', date=0,duree = 0): #Un Dvd est un médium avec une durée
        super().__init__(titre, auteur, date)
        self.duree = duree
    def __str__(self): #Méthode d'affichage d'un Dvd
        return f'{self.titre} de {self.auteur},{self.date_parution},{self.duree} min'
    
    def input_dvd(self): #Méthode d'ajout d'un Dvd
        self.input_medium()
        self.duree = int(input("Durée : "))

class Article_de_Magazine(Medium): #Définition de la classe Dvd dérivée de la classe Medium
    def __init__(self , titre='' , auteur='' , date=0 , nom_mag = '' , numero_mag =0 , intervalle_page = [0,0]): #Un Article de Magazine est un médium avec un nom, un numéro de magazine et un intervalle
        super().__init__(titre, auteur, date)
        self.nom_mag = nom_mag
        self.numero_mag = numero_mag
        self.intervalle_page = intervalle_page

    def __str__(self): #Méthode d'affichage d'un article
        return f'{self.titre} de {self.auteur},{self.date_parution},dans {self.nom_mag} N°{self.numero_mag} {self.intervalle_page[0]}-{self.intervalle_page[1]} '

    def input_mag(self): #Méthode d'ajout d'un article
        self.input_medium()
        self.nom_mag = input("Nom du magazine : ")
        self.numero_mag = int(input("N° : "))
        self.intervalle_page = [int(input("Début intervalle : ")),int(input("Fin intervalle : "))]
    

class Mediatheque(object): #Dénition de la classe servant de simulation d'une Mediatheque
    def __init__(self,list_medium=[]): #La classe possède un seul argument : une liste de médiums
        self.list_medium = list_medium
    
    def __ajouter_medium (self,medium : Medium): #Méthode d'ajout d'un medium
        self.list_medium.append(medium)

    def __recherche_auteur(self,auteur: str): #Méthode de recherche de l'ensemble des mediums d'un même auteur
        for medium in self.list_medium :
            if medium.auteur == auteur :
                print(medium)
    
    def __supprimer_medium(self,titre : str,auteur:str) : #Méthode de suppression d'un médium
        i=0
        for medium in self.list_medium :
            if medium.auteur == auteur and medium.titre == titre :
                supp=self.list_medium.pop(i)
                print(supp,' a bien été supprimé')
                return i        #retourne l'indice où était placé l'élément
            i+=1
        print('Aucun medium de ce type dans la médiathèque')
        return -1               #éléments pas dans la médiathéque
    
    def __supprimer_auteur(self,auteur : str): #Méthode de suppression des mediums d'un auteur
        i=0
        for medium in self.list_medium :   
            if medium.auteur == auteur:
                supp=self.list_medium.pop(i)
                print(supp,' a bien été supprimé')
            i+=1
      
    def __pret(self,nom_pret : str, titre : str, auteur :str): #Méthode d'ajout d'un prêt
        for medium in self.list_medium :
            if medium.auteur == auteur and medium.titre == titre :
                medium._Medium__ajouter_pret(nom_pret)
                return 1
        print('Aucun medium de ce type dans la médiathèque')
        return 0

    def __compte_pret(self): #Méthode de comptage des prêteurs
        res = 0
        for medium in self.list_medium :
            if medium.nom_pret != '' :
                res += 1
        return res

    def __ajouter_input(self): #Méthode d'ajout de médium par le terminal
        
        a=input("Quelle medium ?")
        match a :
            case "Medium" :
                c=Medium()
                c.input_medium()
            
            case "Livre" :
                c=Livre()
                c.input_livre()
            
            case "DVD" :
                c=Dvd()
                c.input_dvd()
            
            case "CD" :
                c=Cd()
                c.input_cd()

            case "Article" :
                c=Article_de_Magazine()
                c.input_mag()

            case _:
                print('Mauvais imput')
                exit()

        self.list_medium.append(c)
        print("J'ai bien ajouté",c)
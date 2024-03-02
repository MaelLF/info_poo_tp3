import unittest
from unittest import mock
import io
from classdef import *


#Auteur : Le Floch Mael
#Date de création : 26 Février 2024

#Objectif du programme : Création de classes permettant les tests unitaires des fonctions de la Classe Mediatheque

class TestMediatheque(unittest.TestCase):
    def setUp(self):
        self.mediatheque = Mediatheque()

    def test_ajouter_medium(self):
        livre = Livre("A", "A", 1, 1, "A")
        self.mediatheque._Mediatheque__ajouter_medium(livre)
        self.assertIn(livre, self.mediatheque.list_medium)

    def test_supprimer_medium(self):
        livre = Livre("2", "2", 2, 2, "2")
        self.mediatheque.list_medium.append(livre)
        index = self.mediatheque._Mediatheque__supprimer_medium("2", "2")
        self.assertNotIn(livre, self.mediatheque.list_medium)

    def test_recherche_auteur(self):
        livre1 = Livre("His", "Jean", 2022, 200, "Ed1")
        livre2 = Livre("Toire", "Jean", 2022, 250, "Ed2")
        self.mediatheque.list_medium.extend([livre1, livre2])

        expected_output = f'His de Jean,2022,200 pages, Ed1\nToire de Jean,2022,250 pages, Ed2\n'
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.mediatheque._Mediatheque__recherche_auteur("Jean")
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_pret(self):
        livre = Livre("Titre", "Auteur", 2022, 300, "Publisher")
        self.mediatheque.list_medium.append(livre)
        self.mediatheque._Mediatheque__pret("John", "Titre", "Auteur")
        
        self.assertEqual(livre.nom_pret,"John")

    def test_compte_pret(self):
        livre1 = Livre("Book1", "Author", 2022, 200, "Publisher1")
        livre2 = Livre("Book2", "Author", 2022, 250, "Publisher2")
        livre2.nom_pret = "John"
        self.mediatheque.list_medium.extend([livre1, livre2])
        self.assertEqual(self.mediatheque._Mediatheque__compte_pret(), 1)

    def test_ajouter_input(self):
        with unittest.mock.patch('builtins.input', side_effect=["Livre", "Rappel", "Marc", "2022", "300", "Publique"]):
            self.mediatheque._Mediatheque__ajouter_input()
        self.assertEqual(len(self.mediatheque.list_medium), 1)

if __name__ == '__main__':
    unittest.main()

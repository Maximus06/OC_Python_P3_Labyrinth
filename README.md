# PROJET MACGYVER

## 1 - Pré-requis
*  **Python 3.7.x**.
* pygame 1.9.6

### Installation 
* Télécharger le repository.
  - `git clone https://github.com/Maximus06/OC_Python_P3_Labyrinth.git`
* Utiliser un **environnement virtuel** est recommandé.
    * Exécuter la ligne de commande : `python3 -m venv <path/to/virtual/environment>`
    puis `source <path/to/venv>/bin/activate` depuis MacOS  
    ou `<path\to\venv>\Scripts\activate.bat`depuis Windows
* Installer les dépendances : `pip install -r requirements.txt`

## 2 - Lancer le programme 
* Exécuter : `python main.py`  depuis la console

--------

## Organisation du code
Le code est  construit en s'inspirant du design pattern MVC et est organisé en package.

### fichiers à la racine du jeu
* **main.py** est le fichier d'entrée du jeu.
* **settings.py** contient les constantes et paramètres du jeu 

### Le package models
Ce package contient les classes représentant les entités principales du jeu:
* **map.py** : contient la classe qui représente le labyrinthe.
* **hero.py** : contient la classe qui représente MacGyver.
* **item.py** : contient la classe qui représente un objet du labyrinthe.
* **position.py** : représente une position dans le labyrinthe.
* **factory.py** : contient les 'factories methods' pour la classe view et l'image d'un item.

### Le package views
Ce package contient les classes en charge de l'affichage
* **view.py** : contient la classe en charge de l'affichage pour la librairie pygame.

### Le package controllers
Ce package contient les classes en charge du rôle de controlleur.
* **game.py** : contient la classe faisant office de controlleur principal. La classe Game fait office de 'glue' pour les autres classes.

### Le dossier .ressources
Il contient les images et sons pour le jeu ainsi que le fichier data/labyrinth.txt contenant la structure du labyrinthe.





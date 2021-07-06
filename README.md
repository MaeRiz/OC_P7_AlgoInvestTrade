# AlgoInvest&Trade

Le but de ce projet est de créer un algorithme rapide en python pour trouver la meilleure combinaison d'actions sur lesquelles investir pour avoir le meilleur bénéfice au bout de 2 ans en prenant en compte les contraintes telles que le montant maximum d'investissement, le prix à virgule des actions et des erreurs de saisie dans les fichiers.

## Prérequis

Installer [Python 3](https://www.python.org/downloads/).


## Utilisation
1. Lancer le programme avec en paramètre le fichier
```cmd
python bruteforce.py nom_du_fichier.csv
python optimized.py nom_du_fichier.csv
```

## Informations

### Fichier: bruteforce.py
Cet algorithme va tester toutes les combinaisons possibles une à une, ce qui rend l'exécution très longue.

### Fichier: optimized.py
Cet algorithme arrondit le prix des actions au supérieur une dizaine après la virgule pour accélérer son exécution.
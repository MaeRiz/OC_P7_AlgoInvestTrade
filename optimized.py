import sys
import csv
import time
from math import ceil

start_time = time.time()

MAX_PRICE = 500                 # Prix d'achat maximum


# Calcul la somme des prix d'une liste d'actions
def somme(lst):
    _sum = []
    for item in lst:
        _sum.append(item[1])
    return (sum(_sum))


# ===========================================================================
#   Fabrication de la matrice et récupération de la meilleur combinaison
# ===========================================================================
def sacADos(lst):

    price = MAX_PRICE*10

    matrice = [[0 for x in range(price + 1)] for x in range(len(lst) + 1)]

    for item in range(1, len(lst) + 1):
        for euro in range(1, price + 1):
            if lst[item-1][1] <= euro:
                matrice[item][euro] = max(
                    lst[item-1][2] + matrice[item-1][euro-lst[item-1][1]],
                    matrice[item-1][euro]
                )
            else:
                matrice[item][euro] = matrice[item-1][euro]

    p = price
    n = len(lst)
    comb = []

    while p >= 0 and n >= 0:
        e = lst[n-1]
        if matrice[n][p] == matrice[n-1][p-e[1]] + e[2]:
            comb.append(e)
            p -= e[1]

        n -= 1

    print('Meilleurs combinaison trouvée: ')
    for c in comb:
        print(c[0])
    print('Prix: ~', somme(comb)/10, '€')
    print('Bénéfice: +', matrice[-1][-1], '€ au bout de 2 ans.')
    print('Exécution: ', time.time() - start_time, "secondes")


# ===========================================================================
#   Traitement du fichier mis en paramètre, convertion en liste exploitable
# ===========================================================================
try:
    with open(sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        actions_lst = []
        for rows in actions:
            if float(rows[1]) <= 0:
                pass
            else:
                actions_lst.append(
                    [
                        rows[0],
                        int(ceil(float(rows[1])*10)),
                        float(float(rows[1]) * float(
                            rows[2].replace('%', '')) / 100),
                    ]
                )

        sacADos(actions_lst)

except FileNotFoundError:
    print("Le fichier n'existe pas. Veuillez vérifier le nom.")

from itertools import combinations
import sys
import csv
import time

start_time = time.time()

MAX_PRICE = 500                 # Prix d'achat maximum


# Calcul le bénéfice a partir d'une liste d'actions
def calc_benef(lst):
    calc = []
    for act in lst:
        calc.append(act[1] * act[2] / 100)
    return (sum(calc))


# Calcul la somme des prix d'une liste d'actions
def somme(lst):
    _sum = []
    for item in lst:
        _sum.append(item[1])
    return (sum(_sum))


# =============================================
# Création et test de toutes les combinaisons
# =============================================
def make_sol(lst):

    actions_lst = lst
    benef = 0

    for i in range(len(actions_lst)):

        combs = combinations(actions_lst, i + 1)
        for comb in combs:
            _sum = somme(comb)
            if _sum <= MAX_PRICE:
                _benef = calc_benef(comb)

                if _benef > benef:
                    benef = _benef
                    best_comb = comb

    print('Meilleurs combinaison trouvée: ')
    for comb in best_comb:
        print(comb)
    print('Prix: ', somme(best_comb), '€')
    print('Bénéfice: +', benef, '€ au bout de 2 ans.')
    print('Exécution: ', time.time() - start_time, "secondes")


# ===========================================================================
#   Traitement du fichier mis en paramètre, convertion en liste exploitable
# ===========================================================================
try:
    with open(sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        actions_lst = []
        for rows in actions:
            actions_lst.append(
                [
                    rows[0],
                    float(rows[1]),
                    float(rows[2].replace('%', ''))
                ]
            )

        make_sol(actions_lst)

except FileNotFoundError:
    print("Le fichier n'existe pas. Veuillez vérifier le nom.")

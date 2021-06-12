from itertools import combinations
import sys
import csv

MAX_PRICE = 500

actions_lst = []

def calc_benef(lst):
    calc = []
    for act in lst:
        calc.append(int(act[1]) * int(act[2].replace('%', '')) / 100)
    return (sum(calc))


def somme(lst):
    _sum = []
    for l in lst:
        _sum.append(int(l[1]))
    return (sum(_sum))


def make_sol():

    benef = 0

    for l in range(len(actions_lst)):

        combs = combinations(actions_lst, l + 1)
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


try:
    with open (sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=';', quotechar='|')
        for rows in actions:
            actions_lst.append([rows[0], rows[1], rows[2]])

        make_sol()

except FileNotFoundError:
    print("Le fichier n'existe pas. Veuillez vérifier le nom.")

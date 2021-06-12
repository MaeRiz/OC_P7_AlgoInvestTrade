import sys
import csv

MAX_PRICE = 500


def calc_benef(lst):
    calc = []
    for act in lst:
        calc.append(act[1] * act[2] / 100)
    return (sum(calc))


def takeThird(elem):
    return elem[2]


def make_sol(lst):
    
    actions_lst = lst
    comb = []
    price = 0
    actions = sorted(actions_lst, key=takeThird, reverse=True)

    for act in actions:
        if price == MAX_PRICE:
            break
        elif act[1] <= 0:
            pass
        elif (price + act[1]) > MAX_PRICE:
            pass
        else:
            comb.append(act)
            price += act[1]

    print('Meilleurs combinaison trouvée: ')
    for c in comb:
        print(c)
    print('Prix: ', price, '€')
    print('Bénéfice: +', calc_benef(comb), '€ au bout de 2 ans.')


try:
    with open (sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        actions_lst = []
        for rows in actions:
            actions_lst.append(
                [rows[0],
                float(rows[1]),
                float(rows[2].replace('%', ''))]
            )
        
        make_sol(actions_lst)

except FileNotFoundError:
    print("Le fichier n'existe pas. Veuillez vérifier le nom.")

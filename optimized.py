import os
import csv
import itertools


def getData():
    while True:
        doc_path = input("Input the .csv file path here: ")

        # Check if doc ends with .csv
        if doc_path.endswith('.csv'):

            # Check if such file exist
            if os.path.isfile(doc_path):
                with open(doc_path, 'r') as file:
                    field_names = ['name', 'price', 'profit']
                    d_reader = csv.DictReader(file)
                    headers = d_reader.fieldnames

                    # Check if the csv header's elements are the right ones
                    if headers == field_names:
                        print("Data is readable, thanks for the input.")
                        return doc_path
                    else:
                        print("Wrong kind of dataset.")
            else:
                print("This file doesn't exist. Check for typos.")
        else:
            print("This isn't a .csv file.")


def csvRowIntoList(csv_doc_path):
    with open(csv_doc_path, 'r') as file:
        print('Collecting data ...')
        file_read = csv.reader(file)
        file_into_list = list(file_read)

        # remove the header's element
        del file_into_list[0]

        # Not only does it take each row into it's own list
        # It also add 2 element in each:
        # [3] is the profit after 2 year
        # [4] is the new total of profit
        for data in file_into_list:
            cost_to_buy = float(data[1])
            profit_percentage = float(data[2].removesuffix("%"))
            benefit = (cost_to_buy*profit_percentage)/100
            profit = cost_to_buy + benefit
            data.append(benefit)
            data.append(profit)
        return file_into_list

# Idées optimisation:
# TODO: 1. Utiliser de la récursion
# Desc: Multiplier les fonctions pour gagner en temps contre de la mémoire
# Solu: ???

# TODO: 2. Enlever les combos trop haut;
# Desc: Le script n'as aucunement besoin d'essayer toutes les combos.
# Solu: Trier la liste par élément "cout", avec ".sort()".
# Additioner les éléments de [0] à son prochain.
# Une fois que la valeur > que 500, alors ...
# (valeur-1) = la range du loop

# TODO: 3. Ne pas faire de répétition;
# Desc: Ne pas dupliquer ex: [1,2] & [2,1]
# Solu: Utiliser ".combinations()" plutôt que ".permuations()"

# TODO: 4. Créer des conditions permettant de trouver le "best";
# Desc: Peut-être que je peux faire en sorte de trouver un élément qui
# est strictement meilleur que les autres et qui doit, à 100% être ajouter ?
# Solu: ???

# TODO: 5. Enlever les données négatives


def comboGenerator(list_of_actions):
    print("Generating combination ...")
    max_profit = 0

    for i in range(1, len(list_of_actions)+1):
        for subset in itertools.combinations(list_of_actions, i):
            actions_names = []
            actions_cost = 0
            actions_benefit = 0
            actions_profit = 0

            for list in subset:
                x = float(list[1])
                actions_cost += x

            if actions_cost < 500:
                for list in subset:
                    name = list[0]
                    benefit = float(list[3])
                    profit = float(list[4])

                    actions_names.append(name)
                    actions_benefit += benefit
                    actions_profit += profit
            else:
                continue

            if max_profit < actions_profit:
                max_profit = actions_profit
                output_new_best(
                    actions_names,
                    actions_cost,
                    actions_benefit,
                    actions_profit)
            else:
                continue


def newBest(max_profit, action_benefit):

    if action_benefit > max_profit:
        max_profit = action_benefit
        return max_profit
    else:
        max_profit = 0
        return max_profit


def output_new_best(names, cost, benefit, profit):
    formated_cost = "{:.2f}".format(cost)
    formated_benefit = "{:.2f}".format(benefit)
    formated_profit = "{:.2f}".format(profit)

    print("")
    print("New best!!")
    print("Best combo is: " + str(names)[1:-1])
    print("For a buying cost of: " + str(formated_cost) + "€")
    print("You get a benefit of: " + str(formated_benefit) + "€")
    print("For a new total of: " + str(formated_profit) + "€")
    print("")


def opti():
    csv_path = getData()
    data_list = csvRowIntoList(csv_path)
    comboGenerator(data_list)
    print("Done")


if __name__ == "__main__":
    opti()

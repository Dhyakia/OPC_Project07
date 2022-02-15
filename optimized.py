import os
import csv
import itertools


MAX_COST = 500


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
        list_index = []
        print("Number of value taken before sort:" + str(len(file_into_list)))
        # remove the header's element
        del file_into_list[0]

        # Add 2 parameter in each element:
        # [3] is the profit after 2 year
        # [4] is the new total of profit
        for data in file_into_list:
            cost_to_buy = float(data[1])
            file_index = file_into_list.index(data)
            if cost_to_buy > 0:
                profit_percentage = float(data[2].removesuffix("%"))
                benefit = (cost_to_buy*profit_percentage)/100
                profit = cost_to_buy + benefit
                formated_benefit = "{:.2f}".format(benefit)
                formated_profit = "{:.2f}".format(profit)
                data.append(formated_benefit)
                data.append(formated_profit)
            else:
                list_index.append(file_index)

        list_index.sort(reverse=True)
        for index in list_index:
            del file_into_list[index]

        print("Number of value taken after sort:" + str(len(file_into_list)))
        return file_into_list


def max_range_combos(list):
    print("Calculating maximum range ...")
    cost_list = []
    range_counter = 0

    for i in list:
        cost_list.append(float(i[1]))

    sorted_list = sorted(cost_list)
    print(sorted_list)
    count_counter = 0
    for i in sorted_list:
        count_counter = (count_counter + i)
        range_counter += 1
        if count_counter > MAX_COST:
            return range_counter
        else:
            continue


def comboGenerator(list_of_actions, max_range):
    print("Generating combination ...")
    max_profit = 0

    for i in range(1, max_range):
        for subset in itertools.combinations(list_of_actions, i):
            actions_names = []
            actions_cost = 0
            actions_benefit = 0
            actions_profit = 0

            for list in subset:
                x = float(list[1])
                actions_cost += x

            if actions_cost < MAX_COST:
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
            else:
                continue

# Idées optimisation:
# TODO: 1. Utiliser de la récursion
# Desc: Multiplier les fonctions pour gagner en temps contre de la mémoire
# Solu: ???

# DONE
# TODO: 2. Enlever les combos trop haut;
# Desc: Le script n'as aucunement besoin d'essayer toutes les combos.
# Solu: Trier la liste par élément "cout", avec ".sort()".
# Additioner les éléments de [0] à son prochain.
# Une fois que la valeur > que 500, alors ...
# (valeur-1) = la range du loop

# DONE
# TODO: 3. Ne pas faire de répétition;
# Desc: Ne pas dupliquer ex: [1,2] & [2,1]
# Solu: Utiliser ".combinations()" plutôt que ".permuations()"

# DONE
# TODO: 4. Enlever les données négatives et les zéros


def opti():
    csv_path = getData()
    data_list = csvRowIntoList(csv_path)
    max_range = max_range_combos(data_list)
    comboGenerator(data_list, max_range)
    print("Done")


if __name__ == "__main__":
    opti()

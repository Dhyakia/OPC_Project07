import os
import csv


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
            formated_benefit = "{:.2f}".format(benefit)
            formated_profit = "{:.2f}".format(profit)
            data.append(formated_benefit)
            data.append(formated_profit)
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

# TODO: 4. Enlever les données négatives


def opti():
    csv_path = getData()
    data_list = csvRowIntoList(csv_path)
    print(data_list)


if __name__ == "__main__":
    opti()

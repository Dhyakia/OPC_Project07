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
        del file_into_list[0]

        # Not only does it take each row into it's own list
        # It also add 2 element in each: 
        # [3] is the profit after 2 year
        # [4] is the new total of profit
        for data in file_into_list:
            cost_to_buy = int(data[1])
            profit_percentage = int(data[2].removesuffix("%"))
            profit = (cost_to_buy*profit_percentage)/100
            new_total = cost_to_buy + profit
            data.append(profit)
            data.append(new_total)
            print(data)
        return file_into_list

# 2. Essayer toutes les combinaisons
# A chauqe génération de combinaisons ...
# Si le total des prix > que 500, alors ça dégage.
# Si le total des prix < que 500, ajouter les bénéfices.
# Comparer les bénéfices du nouveau avec l'ancien meilleur,
# puis garder le meilleurs.
# Petit message comme quoi y'as un nouveau meilleur avec la somme.


def brut():
    csv_path = getData()
    data_list = csvRowIntoList(csv_path)
    # Prochaine fonction, essaye toutes les combinaisons


if __name__ == "__main__":
    brut()

import os
import csv


def getData():
    while True:
        doc_path = input("Input the .csv file path here: ")
        if doc_path.endswith('.csv'):
            if os.path.isfile(doc_path):
                with open(doc_path, 'r') as file:
                    field_names = ['name', 'price', 'profit']
                    d_reader = csv.DictReader(file)
                    headers = d_reader.fieldnames
                    if headers == field_names:
                        print("Data is readable, thanks for the input.")
                        return file
                    else:
                        print("Wrong kind of dataset.")
            else:
                print("This file doesn't exist. Check for typos.")
        else:
            print("This isn't a .csv file.")


# Maintenant que j'ai la file, il faut:
# 1. Function qui créer toutes les combinaisons possibles, qui va être la base de la loop
# 2. Passer cette génératon dans une function qui va faire le calcul des rentabilités
# 3. Comparez si la valeur retourner et plus haute que la précédente, et en faire la valeur de référence si c'est le cas.
def comboGenerator(csv_file):
    print('ok')


def brut():
    data_table = getData()
    comboGenerator(data_table)


if __name__ == "__main__":
    brut()

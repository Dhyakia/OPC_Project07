import itertools
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
            data.append(benefit)
            data.append(profit)
        return file_into_list


# Function that tries every single permutation:
# Worst possible way aka "factorial"
# BigO of a factorial: O(n!)
def comboGenerator(list_of_actions):
    print("Generating combination ...")
    max_profit = 0

    for i in range(1, len(list_of_actions)+1):
        for subset in itertools.permutations(list_of_actions, i):
            actions_names = []
            actions_cost = 0
            actions_benefit = 0
            actions_profit = 0

            for list in subset:
                x = float(list[1])
                actions_cost += x

            if actions_cost < 500:
                for list in subset:
                    x = float(list[4])
                    actions_profit += x
            else:
                continue

            if max_profit < actions_profit:
                max_profit = actions_profit
                for list in subset:
                    name = list[0]
                    actions_names.append(name)
                    action_benefit = float(list[3])
                    actions_benefit += action_benefit
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
    print("")
    print("New best!!")
    print("Best combo is: " + str(names)[1:-1])
    print("For a buying cost of: " + str(cost) + "€")
    print("You get a benefit of: " + str(benefit) + "€")
    print("For a new total of: " + str(profit) + "€")
    print("")


def brut():
    csv_path = getData()
    data_list = csvRowIntoList(csv_path)
    comboGenerator(data_list)
    print("Done")


if __name__ == "__main__":
    brut()

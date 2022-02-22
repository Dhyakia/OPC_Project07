import itertools
import os
import csv


MAX_COST = 500


# Get the path to the right .csv document from an input
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


# Takes the .csv path as target
# return of list of containing lists for each row
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


# Take the cost and benefit element in each element in the list
# return a list of all cost, a list of all benefit and the lenght of the list.
def prepareData(data_list):
    ListofCosts = []
    ListofBenefits = []
    NumberofActions = len(data_list)

    for data in data_list:
        ListofCosts.append(float(data[1]))
        ListofBenefits.append(float(data[3]))

    return ListofCosts, ListofBenefits, NumberofActions

# Time complexity: O(n*n!)
# for loop set it as O(n), then the .combinations...
# 

# Space complexity: O(1);
# Pas de récusivité, ou quelconque techniques pour optimiser l'espace.


# The brute force algorithm
def bruteForce(list_of_actions):
    print("Generating combination ...")
    max_profit = 0

    for i in range(0, len(list_of_actions)+1):
        for subset in itertools.combinations(list_of_actions, i):
            actions_names = []
            actions_cost = 0
            actions_benefit = 0
            actions_profit = 0

            for list in subset:
                actions_cost += float(list[1])

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

            # Choose to incorporate the output every loop,
            # to get a better visualisation of the progress,
            # ... and realise it will never when using large pool of input
            if max_profit < actions_profit:
                max_profit = actions_profit
                output_new_best(
                    actions_names,
                    actions_cost,
                    actions_benefit,
                    actions_profit)
            else:
                continue


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


def brut():
    csv_path = getData()
    data_list = csvRowIntoList(csv_path)
    bruteForce(data_list)
    print("Done!")


if __name__ == "__main__":
    brut()

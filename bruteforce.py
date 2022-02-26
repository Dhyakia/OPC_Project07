import os
import csv
import itertools


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
# Return of list of containing lists for each row
def csv_To_List(csv_doc_path):
    with open(csv_doc_path, 'r') as file:
        print('Collecting data ...')
        file_read = csv.reader(file)
        file_into_list = list(file_read)

        # remove the header's element
        del file_into_list[0]

        # Add 2 parameter in each element:
        # [3] is the profit after 2 year
        # [4] is the new total of profit
        for data in file_into_list:
            cost_to_buy = float(data[1])
            data[1] = cost_to_buy
            profit_percentage = float(data[2].removesuffix("%"))
            benefit = (cost_to_buy*profit_percentage)/100
            profit = cost_to_buy + benefit

            data.append(benefit)
            data.append(profit)
        return file_into_list, len(file_into_list)


# List that will store all the combinasions possible
combos = []


# Brute force method
def combosGenerator(data_list, data_size):
    for x in itertools.combinations(data_list, data_size):
        combos.append(x)
    if data_size > 0:
        return combosGenerator(data_list, data_size-1)
    return combos, len(combos)


# Brute force method
def bruteForce(listallCombos, numberofCombos):
    best_combo_actions = []
    best_combo_profit = 0

    for combination in listallCombos:
        total_cost = 0
        bigBucks = 0

        for action in combination:
            total_cost += action[1]
            bigBucks += action[4]

        if total_cost <= MAX_COST and bigBucks > best_combo_profit:
            best_combo_profit = bigBucks
            best_combo_actions = combination

    return best_combo_actions, best_combo_profit


def output_best(best_actions, best_profit):
    actions_names = []
    actions_costs = 0
    actions_benefits = 0
    actions_profits = best_profit

    # First we get data from each element inside the list
    for action in best_actions:
        actions_names.append(action[0])
        actions_costs += float(action[1])
        actions_benefits += float(action[3])

    # Then we format them into a clean format
    formated_names = str(actions_names)[1:-1]
    formated_costs = str("{:.2f}".format(actions_costs))
    formated_benefits = str("{:.2f}".format(actions_benefits))
    formated_profits = str("{:.2f}".format(actions_profits))

    # Finaly, we display them:
    print("")
    print("The best combo of actions is: " + formated_names)
    print("For a total cost of: " + formated_costs + "€")
    print("It yield a profit of: " + formated_benefits + "€")
    print("For a new total of: " + formated_profits + "€")


def brut():
    csv_path = getData()
    data_list, data_size = csv_To_List(csv_path)
    list_all_combos, combos_size = combosGenerator(data_list, data_size)
    best_actions, best_combo_profit = bruteForce(list_all_combos, combos_size)
    output_best(best_actions, best_combo_profit)


if __name__ == "__main__":
    brut()

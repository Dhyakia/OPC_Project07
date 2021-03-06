from operator import itemgetter
import os
import csv


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


def csv_To_List(csv_doc_path):
    with open(csv_doc_path, 'r') as file:
        print('Collecting data ...')
        file_read = csv.reader(file)
        file_into_list = list(file_read)
        list_index = []

        # remove the header element (name,cost,profit)
        del file_into_list[0]
        print("Number of value taken: " + str(len(file_into_list)))

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
                data[2] = profit_percentage

                data.append(formated_benefit)
                data.append(formated_profit)
            else:
                list_index.append(file_index)

        sorted_data = listCulling(file_into_list, list_index)

        print("Number of value after culling: " + str(len(file_into_list)))
        return sorted_data


# Optimisation: removal of the zeros and negatives numbers based on index
def listCulling(list_of_data, list_of_index):
    list_of_index.sort(reverse=True)
    for index in list_of_index:
        del list_of_data[index]

    return list_of_data


# The gluton algorithm
def greed(list):
    print("Glutony in progress ...")
    list_sorted = sorted(list, key=itemgetter(2), reverse=True)
    big_bucks = 0
    best_actions = []

    for action in list_sorted:
        big_bucks += float(action[1])

        if big_bucks <= MAX_COST:
            best_actions.append(action)
        else:
            big_bucks -= float(action[1])

    return best_actions


def display_results(list_of_best_actions):
    actions_names = []
    actions_costs = 0
    actions_benefits = 0
    actions_profits = 0

    # First we get data from each element inside the list
    for action in list_of_best_actions:
        actions_names.append(action[0])
        actions_costs += float(action[1])
        actions_benefits += float(action[3])
        actions_profits += float(action[4])

    # Then we format them into a clean format
    formated_names = str(actions_names)[1:-1]
    formated_costs = str("{:.2f}".format(actions_costs))
    formated_benefits = str("{:.2f}".format(actions_benefits))
    formated_profits = str("{:.2f}".format(actions_profits))

    # Finaly, we display them:
    print("")
    print("The best combo of actions is: " + formated_names)
    print("For a total cost of: " + formated_costs + "???")
    print("It yield a profit of: " + formated_benefits + "???")
    print("For a new total of: " + formated_profits + "???")


def opti():
    csv_path = getData()
    data_list = csv_To_List(csv_path)
    list_best_actions = greed(data_list)
    display_results(list_best_actions)


if __name__ == "__main__":
    opti()

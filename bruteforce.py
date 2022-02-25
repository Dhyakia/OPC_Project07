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
        return file_into_list


def feeder(listofactions):
    print("Chopping data ...")
    listofCosts = []
    listofProfits = []

    for item in listofactions:
        listofCosts.append(item[1])
        listofProfits.append(item[4])

    listsize = len(listofactions)
    print("Chopping done, feeding data to algorithm ...")
    return listofCosts, listofProfits, listsize


# The brute force algorithm
def bruteForce(max_cost, cost, profit, numberofItem):
    # Base case
    if numberofItem == 0 or max_cost == 0:
        return 0

    # If weight of the nth item is more than the maximum capacity,
    # then the item cannot be included in the optimal solution.
    if (cost[numberofItem-1] > max_cost):
        return bruteForce(max_cost, cost, profit, numberofItem-1)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(profit[numberofItem-1] + bruteForce(
            max_cost-cost[numberofItem-1], cost, profit, numberofItem-1),
                   bruteForce(max_cost, cost, profit, numberofItem-1))


# Ouput data in a formated manner for readability
def output_results(bestComboBenefit, bestComboNames):
    print("")
    print("Solution found!")
    print("The best combos of actions is:" + str(bestComboNames)[1:-1])
    print("For a profit of: " + str("{:.2f}".format(bestComboBenefit) + "€"))


def brut():
    csv_path = getData()
    data_list = csv_To_List(csv_path)
    listofCosts, listsofProfits, listsize = feeder(data_list)
    bruteforceBenefits = bruteForce(
        MAX_COST, listofCosts, listsofProfits, listsize)
    # TODO: temporary list until i found out how to get the names.
    bestCombosNames = ["Name-1", "Name-2", "Name-3"]
    output_results(bruteforceBenefits, bestCombosNames)


if __name__ == "__main__":
    brut()

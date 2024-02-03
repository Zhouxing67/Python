import os
import csv
import sys

"""
filename = 'shopping_basket_dataset.csv'
folder_path = './'

file_path = os.path.join(folder_path, filename)
"""


def dataGen(file_path):
    if not os.path.isfile(file_path):
        print("File path invalid!!!")
        sys.exit()
    dataSet = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            dataSet.append(set(row))
    # print(dataSet)
    return dataSet

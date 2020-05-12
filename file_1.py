# Simple TUI app for Case Study #2
import csv
import pandas as pd
with open('Items.csv', 'w') as f1:
    writer = csv.writer(f1)
    writer.writerow(['ITEM_CODE', 'ITEM_NAME', 'PRICE', 'QUANTITY', 'REORDER_QUANTITY'])


def newItem():
    flag = 0
    while flag == 0:
        flag2 = 0
        while True:
            itemCode = str(input('Enter the item code(Alphanumeric):'))
            state = itemCode.isalnum()
            if len(itemCode) != 4:
                print("Try again!")
                print("Item code should be 4 characters and be Alphanumeric!")
                break
            elif itemCode.isdigit() is True or itemCode.isalpha() is True:
                print("Try Again!")
                print("Item code should be an Alphanumeric!")
                break
            nameInput = str(input("Enter the product name: ")).capitalize()
            if len(nameInput) >= 20 or len(nameInput) == 0:
                print("Try again!")
                print("0<Name length<20")
                break
            priceInput = float(input("Enter the price of the product: "))
            quantityInput = int(
                input("Enter the Quantity in stock of the product: "))
            reorderInput = int(input("Enter the reorder level: "))
            if priceInput <= 0 or quantityInput < 0:
                print("Try Again!")
                break
            else:
                insertList = [itemCode, nameInput,
                              priceInput, quantityInput, reorderInput]
                with open('Items.csv', 'a') as fileObject:
                    writer = csv.writer(fileObject)
                    writer.writerow(insertList)
                print("Entry Successfully made!")
                flag2 = 0
                break
        cont = str(input("Do you wish to continue?(y/n): ")
                   ).lstrip(" ").rstrip(" ").lower()
        if cont == "n":
            flag = 1
            break
        else:
            flag = 0


newItem()
df = pd.read_csv('Items.csv')
print(df)

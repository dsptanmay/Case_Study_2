# MADE BY: Tanmay Deshpande
# GRADE: XII
# SECTION: E
# DATE OF COMPLETION: 13-05-2020
# SALES EMULATION PROJECT
import pickle
from tabulate import tabulate
from datetime import date
import subprocess as sp
import sys
import questionary as qr
print(sys.executable)
print(sys.version)
today = date.today()

header_standard = ['ITEM_CODE', 'DESC',
                   'PRICE', 'DISCOUNT', 'QTY', 'REORDER_QTY']
header_purchase = ['ITEM_CODE', 'DESC', 'PRICE',
                   'DISCOUNT', 'ACTUAL PRICE', 'QTY', 'TOTAL_PRICE']


def createFiles():
    f = open('Items.dat', 'wb')
    f.close()
    f = open('Sales.dat', 'wb')
    f.close()


def newItem():
    cont = 'y'
    while cont in 'yY':
        print('-'*45)
        codes = {}  # Dict to hold item code and index of same
        data = []
        with open('Items.dat', 'rb') as fileObject:
            while True:
                try:
                    data = pickle.load(fileObject)
                    if len(data) == 0:
                        pass
                    else:
                        for row in data:
                            index = data.index(row)
                            ncode = row[0]
                            c = {ncode: index}
                            codes.update(c)
                except:
                    break
        while True:
            code = str(input('Enter the item code:'))  # 1
            if code in codes.keys():
                print('Code already taken!')
                print('Try Again!')
            elif code.isalnum() is False or len(code) != 4:
                print('Try Again!')
            else:
                break
        descInput = str(
            input("Enter a short description of the item: "))  # 2
        desc = descInput[:20]
        while True:
            priceInput = float(input("Enter the price of the item: "))  # 3
            if priceInput < 0:
                print('Try again!')
            else:
                break
        while True:
            discInput = float(input("Enter the discount(in %): "))  # 4
            if discInput < 0:
                print('Try Again!')
            else:
                break
        while True:
            qtyInput = int(input("Enter the current quantity: "))  # 5
            if qtyInput < 0:
                print('Try Again!')
            else:
                break
        while True:
            reQtyInput = int(input('Enter the reorder quantity: '))  # 6
            if reQtyInput < 0:
                print('Try Again!')
            else:
                break
        ins = [code, descInput, priceInput,
               discInput, qtyInput, reQtyInput]
        data.append(ins)
        with open('Items.dat', 'wb') as fileObject:
            pickle.dump(data, fileObject)
        print('Entry successfully made!')
        cont = str(input("Do you wish to continue?(y/n): "))


def modifyItem():
    cont = 'y'
    while cont in 'yY':
        print("-"*45)
        data = []
        codes = {}
        with open('Items.dat', 'rb') as fileObject:
            while True:
                try:
                    data = pickle.load(fileObject)
                    if len(data) == 0:
                        pass
                    else:
                        for row in data:
                            index = data.index(row)
                            ncode = row[0]
                            c = {ncode: index}
                            codes.update(c)
                except:
                    break
        if len(data) == 0:
            print('Data Set is currently empty')
            print('Add some data first!')
            return
        else:
            print('Current data set:\n')
            print(tabulate(data, header_standard, 'fancy_grid'), '\n')

        while True:
            modCode = str(
                input("Enter the code for the item to be modified: "))
            if modCode not in codes.keys():
                print('Invalid Code!\n')
            else:
                modIndex = codes[modCode]  # Gets index of row to be modified
                rec = data[modIndex]  # Gets row to be modified
                print('Entry that is going to be modified:\n')
                print(rec)
                newData = rec
                data.pop(modIndex)
                break
        newDesc = str(input("Enter the NEW Desc(Enter for skip): "))
        if newDesc == "":
            pass
        else:
            newData[1] = newDesc

        while True:
            newPrice = str(input('Enter the NEW Price(Enter for skip): '))
            if newPrice == '':
                break
            elif float(newPrice) < 0:
                print('Price cannot be negative!')
            else:
                newPrice = float(newPrice)
                newData[2] = newPrice

        while True:
            newDisc = str(input('Enter the NEW Discount(Enter for skip): '))
            if newDisc == '':
                break
            elif float(newDisc) < 0:
                print('Discount cannot be negative!')
            else:
                newDisc = float(newDisc)
                newData[3] = newDisc
        while True:
            newQty = str(input('Enter the NEW Quantity(Enter for skip): '))
            if newQty == '':
                break
            elif int(newQty) < 0:
                print('Quantity cannot be negative!')
            else:
                newQty = int(newQty)
                newData[4] = newQty
        while True:
            newReQty = str(
                input('Enter the NEW Reorder Quantity(Enter for skip): '))
            if newReQty == '':
                break
            elif int(newReQty) < 0:
                print('Reorder Quantity cannot be negative!')
            else:
                newReQty = float(newReQty)
                newData[5] = newReQty

        data.insert(modIndex, newData)
        with open('Items.dat', 'wb') as fileObject:
            pickle.dump(data, fileObject)
        print('Entry modified succesfully!')

        cont = str(
            input('Do you wish to continue?(y/n): '
                  )).lower().rstrip(" ").lstrip(" ")


def removeItem():

    data = []
    codes = {}
    with open('Items.dat', 'rb') as fileObject:
        while True:
            try:
                data = pickle.load(fileObject)
                if len(data) == 0:
                    pass
                else:
                    for row in data:
                        index = data.index(row)
                        ncode = row[0]
                        c = {ncode: index}
                        codes.update(c)
            except:
                break
    if len(data) == 0:
        print('Data Set is currently empty')
        print('Add some data first!')
        return
    cont = 'y'
    while cont in 'yY':
        print('-'*45)
        print('Current records:\n')
        print(tabulate(data, header_standard, 'fancy_grid'), '\n')
        while True:
            remCode = str(
                input('Enter the code for which you want to delete the record: '))
            if remCode not in codes.keys():
                print('Invalid Code!')
            else:
                break
        remIndex = codes[remCode]
        data.pop(remIndex)
        newData = data
        with open('Items.dat', 'wb') as fileObject:
            pickle.dump(newData, fileObject)
        print('Modified records:')
        print(tabulate(newData, header_standard, 'fancy_grid'), '\n')
        cont = str(
            input('Do you wish to continue?(y/n): '
                  )).lower().rstrip(" ").lstrip(" ")


def showAll():
    data = []
    with open('Items.dat', 'rb') as fileObject:
        while True:
            try:
                data = pickle.load(fileObject)
            except:
                break
    if len(data) == 0:
        print('Data Set is currently empty')
        print('Add some data first!')
        return
    print('-'*45)
    print(tabulate(data, header_standard, 'fancy_grid'), '\n')


def purchaseItem():
    data = []
    codes = {}
    with open("Items.dat", "rb") as fileObject:
        while True:
            try:
                data = pickle.load(fileObject)
                if len(data) == 0:
                    pass
                else:
                    for row in data:
                        index = data.index(row)
                        ncode = row[0]
                        codes.update({ncode: index})
            except:
                break

    if len(data) == 0:
        print('Data Set is currently empty')
        print('Add some data first!')
        return

    cont = 'y'
    while cont in 'yY':
        print(f"Current data:\n")
        print(tabulate(data, header_standard, 'fancy_grid'), '\n')
        while True:
            purchaseCode = str(
                input("Enter the item code that you want to purchase: "))
            if purchaseCode not in codes.keys():
                print('Invalid code!')
            else:
                index = codes[purchaseCode]
                rec = data[index]
                break
        discount = rec[3]
        acDisc = (discount/100)  # Converting discount from float to percent
        actualPrice = (rec[2] - (rec[2]*acDisc))  # Price - Price*Discount
        while True:
            qty = int(input('Enter the quantity(INT): '))
            if qty < 0:
                print('Value cannot be negative!')
            elif qty >= 0:
                break
        totalPrice = actualPrice*qty
        newList = [purchaseCode, rec[1], rec[2],
                   rec[3], actualPrice, qty, totalPrice]
        with open('Sales.dat', 'ab') as fileObject:
            pickle.dump(newList, fileObject)
        contentList = []
        contentList.append(newList)
        print(today)
        print('\n')
        print(tabulate(contentList, header_purchase, 'fancy_grid'), '\n')
        print("- Thank you for shopping with us! ")
        print("- No returns,no refunds ")
        print("- If cashier doesn't provide the bill, then this purchase is on the house\n")
        cont = str(input('\nDo you wish to continue?(y/n): ')
                   ).lower().rstrip(" ").lstrip(" ")


def main():
    createFiles()
    options = ['1.Add a new item',
               '2.Modify an existing item',
               '3.Remove an exisiting item',
               '4.Show all items',
               '5.Purchase an item and generate a bill',
               '6.EXIT']
    while True:
        print('-'*50)
        question = qr.select(
            'Select from one of the options: ',
            choices=options)
        response = question.ask()
        if response == options[0]:
            newItem()
        elif response == options[1]:
            modifyItem()
        elif response == options[2]:
            removeItem()
        elif response == options[3]:
            showAll()
        elif response == options[4]:
            purchaseItem()
        elif response == options[5]:
            exit()


if __name__ == "__main__":
    main()

# CSV VERSION OF SALES EMULATION PROJECT
import csv
import sys
from datetime import date
import subprocess as sp
import pkg_resources
required = {'tabulate', 'questionary'}
installed_pkgs = {pkg.key for pkg in pkg_resources.working_set}
missing = required-installed_pkgs
if missing:
    python = sys.executable
    sp.check_call([python, '-m', 'pip', 'install', '--upgrade',
                   *missing], stdout=sp.DEVNULL)
    from tabulate import tabulate
    import questionary as qr
else:
    from tabulate import tabulate
    import questionary as qr

print(sys.executable)
print(sys.version)
today = date.today()
header_standard = ['ITEM_CODE', 'DESC',
                   'PRICE', 'DISCOUNT', 'QTY', 'REORDER_QTY']
header_purchase = ['ITEM_CODE', 'DESC', 'PRICE',
                   'DISCOUNT', 'ACTUAL PRICE', 'QTY', 'TOTAL_PRICE']


def createFiles():
    f = open('Items.csv', 'w')
    f.close()
    f = open('Sales.csv', 'w')
    f.close()


def newItem():
    cont = True
    while cont:
        print('-'*45)
        data = []
        codes = {}
        with open('Items.csv', 'r') as fileObject:
            reader = csv.reader(fileObject)
            for line in reader:
                if len(line) != 0:
                    data.append(line)
            if len(data) != 0:
                for row in data:
                    index = data.index(row)
                    ncode = row[0]
                    c = {ncode: index}
                    codes.update(c)
        if len(data) != 0:
            print('Current Data:\n')
            print(tabulate(data, header_standard, 'fancy_grid'), '\n')
        while True:
            codeInput = str(input('Enter the item code: '))
            if codeInput in codes.keys():
                print('This Code has already been used')
                print('Try Again!')
            elif codeInput.isalnum() is False or len(codeInput) != 4:
                print('Code should be alphanumeric and 4 chars!')
            else:
                break

        descInput = str(input('Enter a short description of the item: '))
        if descInput == '':
            pass
        else:
            descInput = descInput[:20]

        while True:
            priceInput = float(input('Enter the price of the item: '))
            if priceInput <= 0:
                print('Price cannot be 0 or negative!')
            else:
                break

        while True:
            discInput = float(input('Enter the discount in %: '))
            if discInput < 0:
                print('Discount cannot be negative!')
            else:
                break

        while True:
            qtyInput = int(input('Enter the current quantity of the item: '))
            if qtyInput < 0:
                print('Quantity cannot be negative!')
            else:
                break

        while True:
            reQtyInput = int(input('Enter the reorder quantity: '))
            if reQtyInput < 0:
                print('Reorder QTY cannot be negative!')
            else:
                break
        ins = [codeInput, descInput, priceInput,
               discInput, qtyInput, reQtyInput]
        # Opened in append to simply add one row instead of overwriting the entire file
        with open('Items.csv', 'a') as fileObject:
            writer = csv.writer(fileObject)
            writer.writerow(ins)
            print('Entry successfully inserted!')
        print('-'*45)
        cont = qr.confirm('Do you wish to continue?').ask()


def modifyItem():
    cont = True
    while cont:
        data = []
        codes = {}
        with open('Items.csv', 'r') as fileObject:
            reader = csv.reader(fileObject)
            for line in reader:
                if len(line) != 0:
                    data.append(line)
            if len(data) != 0:
                for row in data:
                    index = data.index(row)
                    ncode = row[0]
                    c = {ncode: index}
                    codes.update(c)
        if len(data) == 0:
            print('Data Set is Currently empty')
            print('Add some data first!')
            return
        else:
            print('Current data:\n')
            print(tabulate(data, header_standard, 'fancy_grid'), '\n')

        while True:
            codeInput = str(
                input('Enter the code for which you want to modify: '))
            if codeInput not in codes.keys():
                print('Invalid code')
                print('Try again!')
            else:
                modIndex = codes[codeInput]  # gets index of row to be modified
                modRecord = data[modIndex]  # Gets record to be modified
                newData = modRecord
                data.pop(modIndex)
                break

        newDesc = str(input("Enter the new description(Enter for skip): "))
        if newDesc == '':
            pass
        else:
            newDesc = newDesc[:20]
            newData[1] = newDesc

        while True:
            newPrice = str(input('Enter the NEW Price(Enter for skip): '))
            if newPrice == '':
                break
            elif float(newPrice) < 0:
                print('Price cannot be negative')
            else:
                newPrice = float(newPrice)
                newData[2] = newPrice
                break
        while True:
            newDisc = str(input('Enter the new discount(Enter for skip): '))
            if newDisc == '':
                break
            elif float(newDisc) < 0:
                print('Discount cannot be negative!')
            else:
                newDisc = float(newDisc)
                newData[3] = newDisc
                break

        while True:
            newQty = str(
                input('Enter the NEW current Quantity(Enter for skip): '))
            if newQty == '':
                break
            elif int(newQty) < 0:
                print('Quantity cannot be negative!')
            else:
                newQty = int(newQty)
                newData[4] = newQty
                break

        while True:
            newReQty = str(
                input('Enter the NEW reorder quantity(Enter for skip): '))
            if newReQty == "":
                break
            elif int(newReQty) < 0:
                print('Reorder Quantity cannot be negative!')
            else:
                newReQty = int(newReQty)
                newData[5] = newReQty
                break

        data.insert(modIndex, newData)
        print('Record successfully modified!')
        with open('Items.csv', 'w') as fileObject:
            writer = csv.writer(fileObject)
            for row in data:
                writer.writerow(row)
        cont = qr.confirm('Do you wish to continue?').ask()


def removeItem():
    cont = True
    while cont:
        data = []
        codes = {}
        with open('Items.csv', 'r') as fileObject:
            reader = csv.reader(fileObject)
            for line in reader:
                if len(line) != 0:
                    data.append(line)
            if len(data) != 0:
                for row in data:
                    index = data.index(row)
                    ncode = row[0]
                    c = {ncode: index}
                    codes.update(c)

        if len(data) == 0:
            print('Data set is currently empty')
            print('Add some data first!')
            return
        else:
            print('Current data:\n')
            print(tabulate(data, header_standard, 'fancy_grid'), '\n')

        while True:
            codeInput = str(
                input('Enter the code for which you want to delete: '))
            if codeInput not in codes.keys():
                print('Invalid Code\nTry Again!')
            else:
                remIndex = codes[codeInput]
                data.pop(remIndex)
                newData = data
                break
        print('Entry successfully deleted!\n')
        print(tabulate(newData, header_standard, 'fancy_grid', '\n'))
        with open('Items.csv', 'w') as fileObject:
            writer = csv.writer(fileObject)
            for row in newData:
                writer.writerow(row)

        cont = qr.confirm('Do you wish to continue?')


def showAllItems():
    data = []
    with open('Items.csv', 'r') as fileObject:
        reader = csv.reader(fileObject)
        for line in reader:
            if len(line) != 0:
                data.append(line)
    if len(data) != 0:
        print(tabulate(data, header_standard, 'fancy_grid'), '\n')
    else:
        print('Data set is currently empty')
        print("Add some data first!")
        return


def purchaseItem():
    cont = True
    while cont:
        data = []
        codes = {}
        with open('Items.csv', 'r') as fileObject:
            reader = csv.reader(fileObject)
            for line in reader:
                if len(line) != 0:
                    data.append(line)
                if len(data) != 0:
                    for row in data:
                        index = data.index(row)
                        ncode = row[0]
                        c = {ncode: index}
                        codes.update(c)

        if len(data) == 0:
            print('Data Set is currently empty')
            print('Add some data first!')
            return
        print('Current data:\n')
        print(tabulate(data, header_purchase, 'fancy_grid'), '\n')
        while True:
            codeInput = str(
                input('Enter the code of the item that you want to purchase: '))
            if codeInput not in codes.keys():
                print('Invalid Code\nTry Again!')
            else:
                pIndex = codes[codeInput]
                pRec = data[pIndex]
                break
        description = str(pRec[1])
        price = float(pRec[2])
        discount = float(pRec[3])/100
        actualPrice = price - price*discount

        while True:
            qty = int(input('Enter the quantity: '))
            if qty < 0:
                print("Quantity cannot be negative\nTry Again!")
            else:
                break
        totalPrice = actualPrice*qty
        newList = [codeInput, description, price,
                   discount, actualPrice, qty, totalPrice]
        printedList = []
        printedList.append(newList)
        print('\nBill:\n')
        print(tabulate(printedList, header_purchase, 'fancy_grid'), '\n')
        print("""
                 -Thank you for shopping with us!
                 -NO RETURNS, NO REFUNDS!
                 -IF Bill is not provided, then this purchase is on the house!
                 """)
        cont = qr.confirm('Do you wish to continue?').ask()


def main():
    createFiles()
    options = ['1.Add a new item',
               '2.Modify an existing item',
               '3.Remove an existing item',
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
            showAllItems()
        elif response == options[4]:
            purchaseItem()
        elif response == options[5]:
            exit()
        else:
            print('Try again!')


if __name__ == "__main__":
    main()

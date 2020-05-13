import pickle
import csv
from datetime import date
from tabulate import tabulate


def createFiles():
    f = open('Items.dat', 'wb')
    f.close()
    f = open('Sales.dat', 'wb')
    f.close()


def newItem():
    codes = []
    data = []
    with open('Items.dat', 'rb') as fileobj:
        while True:
            try:
                data = pickle.load(fileobj)
                for i in data:
                    codes.append(i[0])

    cont = 'y'
    while cont in 'yY':
        while True:
            code = str(input('Enter the item code: '))
            if code in codes:
                print('That code already exists!')
            elif len(code) != 4 or not(code.isalnum()):
                print('Try Again!')
            else:
                break
        desc = str(input(prompt='Enter item desc(max 20 chars): '))
        desc = desc[:20]
        price = float(input('Enter the price of the item: '))
        qty = float(input('Enter the current quantity of the item: '))
        reQty = float(input(prompt='Enter the reorder Quantity: '))
        ins = [code, desc, price, qty, reQty]
        data.append(ins)
        cont = str(input('Do you wish to continue?(y/n): ')
                   ).lower().rstrip(" ").lstrip(" ")
    with open('Items.dat', 'ab') as f:
        pickle.dump(data, f)


def removeItem():
    codes = []
    data = []
    with open('Items.dat', 'rb') as f:
        while True:
            try:
                data = pickle.load(f)
                for row in data:
                    codes.append(row[0])

            except:
                break
    more = 'y'
    while more in 'yY':
        while True:
            code = str(
                input('Enter the item code which you wanted to delete: '))
            if code in codes:
                index = 1
                break
            else:
                print('This code does not exist,Please try again!')
        more = str(input('Do you wish to continue?(y/n): '))


createFiles()
f1 = open('Items.dat', 'rb')
data = pickle.load(f1)
print(data)

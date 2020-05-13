import pickle
from tabulate import tabulate
from datetime import date
today = date.today()
# list1 = [['201d', 'Shoes', 9999, 13, 4], ['201e', 'Nite', 8999, 10, 6]]
# with open('Items.dat', 'wb') as f:
#     pickle.dump(list1, f)

f = open('Items.dat', 'wb')
f.close()


def newItem():
    newCodes = []  # For multiple entries at once, we have to store the code
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
    cont = 'y'
    while cont in 'yY':
        while True:
            code = str(input('Enter the item code:'))  # 1
            if code in newCodes or code in codes.keys():
                print('Code already taken!')
                print('Try Again!')
            elif code.isalnum() is False or len(code) != 4:
                print('Try Again!')
            else:
                newCodes.append(code)
                break
        while True:
            descInput = str(
                input("Enter a short description of the item: "))  # 2
            desc = descInput[:20]
            priceInput = float(input("Enter the price of the item: "))  # 3
            discInput = float(input("Enter the discount(in %): "))  # 4
            qtyInput = int(input("Enter the current quantity: "))  # 5
            reQtyInput = int(input('Enter the reorder quantity: '))  # 6
            if priceInput <= 0 or discInput < 0 or qtyInput < 0 or reQtyInput < 0:
                print('Try Again!')
            else:
                ins = [code, descInput, priceInput,
                       discInput, qtyInput, reQtyInput]
                data.append(ins)
                with open('Items.dat', 'wb') as fileObject:
                    pickle.dump(data, fileObject)
                print('Entry successfully made!')
                print('-'*50)
                break
        cont = str(input("Do you wish to continue?(y/n): "))


def modifyItem():
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
        print('Current records:\n')
        print(data, '\n')
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

        newPrice = float(input('Enter the NEW Price(Enter for skip): '))
        if newPrice == '':
            pass
        else:
            newData[2] = newPrice

        newDisc = float(input('Enter the NEW Discount(Enter for skip): '))
        if newDisc == '':
            pass
        else:
            newData[3] = newDisc

        newQty = int(input('Enter the NEW Current Quantity(Enter for skip): '))
        if newQty == '':
            pass
        else:
            newData[4] = newQty

        newReQty = int(
            input("Enter the NEW Reorder Quantity(Enter for skip): "))
        if newReQty == '':
            pass
        else:
            newData[5] == newReQty

        data.insert(modIndex, newData)
        with open('Items.dat', 'wb') as fileObject:
            pickle.dump(data, fileObject)
        print('Entry modified succesfully!')

        cont = str(
            input('Do you wish to continue?(y/n): '
                  )).lower().rstrip(" ").lstrip(" ")


def removeItem():
    codes = {}
    data = []
    with open('Items.dat', 'rb') as f3:
        while True:
            try:
                data = pickle.load(f3)
                if len(data) == 0:
                    print('Enter some data first!')
                    pass
                else:
                    for row in data:
                        index = data.index(row)
                        ncode = row[0]
                        c = {ncode: index}
                        codes.update(c)
                    break
            except:
                break
    cont = 'y'
    newData = []
    while cont in 'yY':
        x = str(input("Enter the code that you want to delete: "))
        if x in codes.keys():
            index = codes[x]
            del codes[x]
            data.pop(index)
            newData = data
            with open('Items.dat', 'wb') as fileObject:
                pickle.dump(newData, fileObject)
            break
        elif x not in codes.keys():
            print('The code entered is not valid. Please Try Again!')
        cont = str(
            input('Do you wish to continue?(y/n): '
                  )).lower().lstrip(" ").rstrip(" ")
        print("-"*50)


def showAll():
    data = []
    heading = ['ITEM_CODE', 'DESC', 'PRICE', 'DISCOUNT', 'QTY', 'REORDER_QTY']
    with open('Items.dat', 'rb') as fileObject:
        while True:
            try:
                data = pickle.load(fileObject)
            except:
                break
    print(tabulate(data, heading, 'fancy_grid'))


def purchaseItem():
    header = ['ITEM_CODE', 'DESC', 'PRICE', 'DISCOUNT',
              'ACTUAL_PRICE', 'QUANTITY', 'TOTAL_PRICE']
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
                    print(f"Current data:{data}")
                    print(f"Codes:{codes}")
            except:
                break
    if len(data) == 0:
        print('Data Set is currently empty')
        print('Enter some data first!')
        return

    cont = 'y'
    while cont in 'yY':
        print("\n")
        while True:
            purchaseCode = str(
                input("Enter the item code that you want to purchase: "))
            if purchaseCode not in codes.keys():
                print('Invalid code!')
            elif purchaseCode in codes.keys():
                index = codes[purchaseCode]
                rec = data[index]
                break
            else:
                break
        discount = rec[3]
        acDisc = (discount/100)
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
        contentList = []
        contentList.append(newList)
        print(today)
        print('\n')
        print(tabulate(contentList, headers=header, tablefmt='fancy_grid'))
        cont = str(input('\nDo you wish to continue?(y/n): ')
                   ).lower().rstrip(" ").lstrip(" ")


def main():
    cont = 'y'
    while cont in 'yY':
        print('\n')
        print("""
                1.Add a new Item
                2.Modify an existing item
                3.Remove an Item
                4.Show all items.
                5.Purchase an item and then generate a bill for it
                6.EXIT
            """)
        opt = int(input("Choose from one of the options above: "))
        if opt not in [1, 2, 3, 4, 5]:
            print('Enter a valid input!')
        elif opt == 1:
            newItem()
        elif opt == 2:
            modifyItem()
        elif opt == 3:
            removeItem()
        elif opt == 4:
            showAll()
        elif opt == 5:
            purchaseItem()
        elif opt == 6:
            exit()
        print("-"*76)
        cont = str(input('Do you wish to continue?(y/n)(Main Menu): '))
        print("-"*76)


if __name__ == "__main__":
    main()
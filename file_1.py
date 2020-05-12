# Simple TUI app for Case Study #2
fileObject1 = open("Items.dat", 'w')
fileObject2 = open('Sales.dat', 'w')


def newItem():
    flag = 0
    while flag == 0:
        flag2 = 0
        while flag2 == 0:
            itemCode = str(input('Enter the item code(Alphanumeric):'))
            state = itemCode.isalnum()
            if len(itemCode) != 4 or itemCode.isdigit() == True or itemCode.isalpha() == True:
                print("Try again!")
                print("Item code should be 4 characters and be Alphanumeric!")
                break
            nameInput = str(input("Enter the product name: "))
            if len(nameInput) >= 20 or len(nameInput) == 0:
                print("Try again!")
                print("Name should be more than 0 chars and less than 20 characters !")
                break
            priceInput = float(input("Enter the price of the product(in ₹): "))
            quantityInput = int(input("Enter the Quantity in stock of the product: "))
            reorderInput = int(input("Enter the reorder level"))
            if priceInput <= 0 or quantityInput < 0 or reorderInput == 0:
                print("Try Again!")
                break
            else:
                insertList = [itemCode, nameInput, priceInput, quantityInput, reorderInput]
                print("Entry Successfully made!")
                flag2 = 0
                break
        cont = str(input("Do you wish to continue?(y/n): ")).lstrip(" ").rstrip(" ").lower()
        if cont == "n":
            flag = 1
            break
        else:
            flag = 0


def modify():

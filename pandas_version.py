import pandas as pd
import csv


def createFiles():
    f = open('Items.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['ITEM_CODE', 'DESC', 'PRICE',
                     'DISCOUNT', 'QTY', 'REORDER_QTY'])
    writer.writerow(['201e', 'Nike Shoes', 9999, 15, 5, 3])
    writer.writerow(['201d', 'Puma Shoes', 8999, 10, 6, 4])
    f.close()
    f = open('Sales.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['ITEM_CODE', 'DESC', 'PRICE', 'DISCOUNT',
                     'ACTUAL_PRICE', 'QTY', 'TOTAL_PRICE'])
    f.close()


def newItem():
    codes = {}
    cont = 'y'
    df = pd.read_csv('Items.csv')
    print(df)
    print(df.values)
    index = 0
    for row in df.values:
        ncode = row[0]
        c = {ncode: index}
        codes.update(c)
        index += 1
    print(codes)


createFiles()
newItem()

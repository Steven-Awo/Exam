import random
import json
from os import remove


def createProducts():
    id = random.randint(1, 10)
    title = input("Enter Product Name: ")
    quantity = input("Enter the Quantity: ")
    price = float(input("Enter the Price: "))

    data = {
        "id": id,
        "title": title,
        "quantity": quantity,
        "price": price
    }

    with open('products.json', 'w+') as fileName:
        json.dump(data, fileName, indent=1)


def readProducts():
    with open('products.json') as fileName:
        data = json.loads(str(fileName.read()))
        print("Name of book", data["title"])
        print("Quantity", data["quantity"])
        print("Price", data["price"])


def updateProducts():
    with open('products.json') as fileName:
        data = json.loads(str(fileName.read()))
        print("Existing data ", data)

        dar = {
            "id": random.randint(1, 10),
            "title": "Bible",
            "quantity": "100",
            "price": 2.0
        }

        with open('products.json', 'w+') as file:
            json.dump(dar, file, indent=1)
            print("\nData has been Updated\n")


def deleteProducts():
    remove('products.json')





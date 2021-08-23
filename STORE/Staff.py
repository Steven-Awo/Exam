import random
import json


def create_acc():
    print("Create an account")
    id = random.randrange(1,50)
    email = input("Enter your Email: ")
    password = input("Enter the Password: ")

    data = {
        "id": id,
        "email": email,
        "password": password
    }

    with open('Staff.jsaon', 'w+') as createfile:
        json.dump(data, createfile)



# def createproducts():
#     print("Create a product")
#     id = random.randrange(1,20)
#     title = input("Enter the name")
#     price =  input("Enter the price")
#     quantity= input("Enter amount")
#
#     inform = {
#
#         "ID": id,
#         "Title": title,
#         "Price": price,
#         "Quantity": quantity
#     }
#
#     with open("products.jsaon","w") as jsonPfile:
#         json.dump(inform,jsonPfile)
#
#
# #------------------------------------------------------
#
# def createsales():
#     print("Create a sale")
#     id = random.randrange(1,20)
#     title = input("Enter the name")
#     price =  input("Enter the price")
#     quantity= input("Enter amount")
#
#     inform = {
#
#         "ID": id,
#         "Title": title,
#         "Price": price,
#         "Quantity": quantity
#     }
#
#     with open("products.jsaon","w") as jsonPfile:
#         json.dump(inform,jsonPfile)
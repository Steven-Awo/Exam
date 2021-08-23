
import os
import json

def login():
    print("\nEnter your login in details\n")
    email = input("Enter your email = ")
    password = input("Enter your password= ")

    with open("C:\\Users\\STEVEN AWOMODDU\\Desktop\\INDUSTRIAL TRAINING\\PYTHON\\EXAMIT\\Staff.jsaon","r") as createjsonfile:
        info = json.loads(createjsonfile.read())

        print(info)
        if email == info["email"] and password == info["password"]:
            print("You were successful")

        else:
            print("Wrong email and password")

            login()


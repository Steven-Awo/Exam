from os  import read
from STORE.Staff import create_acc
from STORE.sales import *
from STORE.products import *
from STORE.Login import login
print(" \n           Python EXAM \n     \n         Rotimi Oluwadurotimi Awomodu \n"
      " ")


def main():
    staffoptions()
    prodoption()
    createsales()

def staffoptions():
    print("""Already Have an account press 'Yes',\nDon't have an account, press 'NO'""")
    choice = input("Enter your Choice: ")

    if choice == "Yes".casefold():
        login()
    elif choice == "No".casefold():
        create_acc()
    else:
        print("\nThis option you picked doesn't not exist\n")
        staffoptions()


def prodoption():
    print(""" If you want to create a product press 1,       to read  a product  press 2,\n 
    to update  a product press 3,            to delete  a product  press 4    """)
    choice = input("Enter your Choice: ")

    if choice == "1":
        createProducts()
    elif choice == "2":
        readProducts()
    elif choice == "3":
        updateProducts()
    elif choice == "4":
        deleteProducts()
    else:
        print("\nPlease Select only between 1 to 4\n")
        prodoption()


if __name__ == '__main__':
    main()












import random

import json
import datetime
from  STORE.products import *

def createsales():
    print("Create a sale")
    with open("C:\\Users\\STEVEN AWOMODDU\\Desktop\\INDUSTRIAL TRAINING\\PYTHON\\EXAMIT\\products.json") as salesfile:
        dat = json.loads(str(salesfile.read()))
        print(dat)


        Sales_date = datetime.datetime.now()
        product_title = dat["title"]
        total_price =  dat["price"]
        quantity_sold= dat["quantity"]

        saleinfo = {
            "date": str(Sales_date),
            "title": product_title,
            "quantity": quantity_sold,
            "price": total_price
        }

        with open("C:\\Users\\STEVEN AWOMODDU\\Desktop\\INDUSTRIAL TRAINING\\PYTHON\\EXAMIT\\Sales.json", "w+") as salesfile:
            json.dump(saleinfo, salesfile, indent=1)

        print(Sales_date)
        print(product_title)
        print(total_price)
        print(quantity_sold)


createsales()
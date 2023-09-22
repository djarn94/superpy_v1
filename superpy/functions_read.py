from datetime import date
import csv
from rich.table import Table
from rich.console import Console
from settings import *
import matplotlib.pyplot as plt
import numpy as np

todaysdate = str(date.today())
##########################################################################################################################################
#overal functions and csv read functions.

#Generates a bought ID
def bought_id():

    id_list = []

    with open('bought.csv', 'r', newline = '') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        for row in rows:      
            id_list.append(row['id'])
        try:
            last_id = int(id_list[-1]) + 1
        except:
            last_id = 1
        return last_id
    
#generates a sold ID
def sold_id():

    id_list = []

    with open('sold.csv', 'r', newline = '') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        for row in rows:
            id_list.append(row['id'])
        try:
            last_id = int(id_list[-1]) + 1
        except:
            last_id = 1
        return last_id

#Shows current inventory and filters out sold and expired items.
def inventory_list():
     
     with open('bought.csv', 'r', newline = '') as file:
         csv_reader = csv.reader(file)
         next(csv_reader)
         list = []
         product_list = []
         id_list = []

         table = Table(title=f'Inventory')
         table.add_column("Product name", justify="left", style="cyan", no_wrap=True)
         table.add_column("Amount", justify="center", style="magenta")

         for row in csv_reader:
            list.append(row)

         for id, item,price,buydate,expdate in list:
            if buydate <= date_today():
                if expdate >= date_today():
                    if id not in sold_boughtid():
                        id_list.append(id)
                        product_list.append(item)

                #if id_list not in sold_boughtid():
         
         product_dict = dict((x, product_list.count(x)) for x in set(product_list))
         for product, amount in product_dict.items():
             table.add_row(product, str(amount))

         return table

#shows all items in bought list and also shows if the product is expired or sold.
def bought_list():
     
     list = []
     
     table = Table(title=f'bought list')
     table.add_column("id", justify="left", style="cyan", no_wrap=True)
     table.add_column("product name", justify="center", style="magenta")
     table.add_column("buy price", justify="center", style="magenta")
     table.add_column("buy date", justify="center", style="magenta")
     table.add_column("expiry date", justify="center", style="magenta")
     table.add_column('expired', justify='center',style='red')
     table.add_column('sold',justify='center',style='green')

     with open('bought.csv', 'r', newline = '') as file:
         csv_reader = csv.reader(file)
         next(csv_reader, None)

         for row in csv_reader:
            list.append(row)

     for id, product, price, date, exp in list:
        if date <= date_today():
            if id in sold_boughtid():
                table.add_row(id, product, price, date, exp, '', 'Y')
            elif exp <= date_today():
                table.add_row(id, product, price, date, exp, 'X')
            else:
                table.add_row(id, product, price, date, exp)

     return table


def sold_list():

     table = Table(title=f'sold list')
     table.add_column("id", justify="left", style="cyan", no_wrap=True)
     table.add_column("bought id", justify="center", style="magenta")
     table.add_column("sell price", justify="center", style="magenta")
     table.add_column("sell date", justify="center", style="magenta")

     with open('sold.csv', 'r', newline = '') as file:
         reader = csv.reader(file)
         next(reader, None)

         for id,boughtid,sell,date in reader:
            if date <= date_today():
                table.add_row(id,boughtid,sell,date)

     return table

#returns boughtid's that are sold.
def sold_boughtid():
     
     list = []

     with open('sold.csv', 'r', newline = '') as file:
         reader = csv.reader(file)
         next(reader, None)

         for id,boughtid,sell,date in reader:
            list.append(boughtid)
            

     return list

#Shows profit of selected date range.
def profit(start_date, end_date):

    sold_list = []
    buy_list = []
    start_date = str(date.fromisoformat(start_date))
    end_date = str(date.fromisoformat(end_date))
    
    with open('bought.csv', 'r', newline = '') as buy_file:
        buy_reader = csv.DictReader(buy_file)

        for row in buy_reader:
            if row['buy_date'] >= start_date and row['buy_date'] <= end_date:
                buy_list.append(float(row['buy_price']))

    with open('sold.csv', 'r', newline = '') as sell_file:
        sold_reader = csv.DictReader(sell_file)

        for row in sold_reader:
            if row['sell_date'] >= start_date and row['sell_date'] <= end_date:
                sold_list.append(float(row['sell_price']))

    sumbuy = round(sum(buy_list),2)
    sumsold = round(sum(sold_list),2)
    profit = round(sumsold - sumbuy,2)

    table = Table(title='Finance overview')
    table.add_column('Expenses', justify='middle', style='cyan')
    table.add_column('Revenue', justify='middle', style='cyan')
    table.add_column('Profit', justify='middle', style='cyan')

    table.add_row(str(sumbuy), str(sumsold),str(profit))

    print(f'selected date range = {start_date} -> {end_date}')
    return table


 ##########################################################################################################################################
 #functions to create the line graph.

#Makes a list to record profit per month for a line graph.
def profit_per_year(year):

    month_1 = float(profit_only(year+"01"+"01",year+"01"+"31"))
    month_2 = float(profit_only(year+"02"+"01",year+"02"+"28"))
    month_3 = float(profit_only(year+"03"+"01",year+"03"+"31"))
    month_4 = float(profit_only(year+"04"+"01",year+"04"+"30"))
    month_5 = float(profit_only(year+"05"+"01",year+"05"+"31"))
    month_6 = float(profit_only(year+"06"+"01",year+"06"+"30"))
    month_7 = float(profit_only(year+"07"+"01",year+"07"+"31"))
    month_8 = float(profit_only(year+"08"+"01",year+"08"+"31"))
    month_9 = float(profit_only(year+"09"+"01",year+"09"+"30"))
    month_10 = float(profit_only(year+"10"+"01",year+"10"+"31"))
    month_11 = float(profit_only(year+"11"+"01",year+"11"+"30"))
    month_12 = float(profit_only(year+"12"+"01",year+"12"+"31"))

    year_list = [month_1, month_2, month_3, month_4, month_5, month_6, month_7, month_8, month_9, month_10, month_11, month_12]
    return year_list

#sub function for profit_per_year returns only profit of selected date range.
def profit_only(start_date, end_date):

    sold_list = []
    buy_list = []
    start_date = str(date.fromisoformat(start_date))
    end_date = str(date.fromisoformat(end_date))
    
    with open('bought.csv', 'r', newline = '') as buy_file:
        buy_reader = csv.DictReader(buy_file)

        for row in buy_reader:
            if row['buy_date'] >= start_date and row['buy_date'] <= end_date:
                buy_list.append(float(row['buy_price']))

    with open('sold.csv', 'r', newline = '') as sell_file:
        sold_reader = csv.DictReader(sell_file)

        for row in sold_reader:
            if row['sell_date'] >= start_date and row['sell_date'] <= end_date:
                sold_list.append(float(row['sell_price']))

    sumbuy = round(sum(buy_list),2)
    sumsold = round(sum(sold_list),2)
    profit = round(sumsold - sumbuy,1)

    return profit

#Shows the profit or loss per year.
def year_overview(year):
    fig, ax = plt.subplots(facecolor = 'lightblue', figsize=(8,6))
    ax.set_title('profit or loss per month', loc='center', fontstyle='oblique', fontsize='medium')
    ax.set_xlabel('Month number')
    ax.set_ylabel('amount in EUR')

    # make data:
    ax.plot([1,2,3,4,5,6,7,8,9,10,11,12], profit_per_year(year))

    return plt.show()

  ##########################################################################################################################################   

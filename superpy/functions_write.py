from datetime import date
import csv
from functions_read import *
from rich.console import Console
from pathlib import *
from settings import *

 ##########################################################################################################################################
 #csv write functions


#to register bought products to the bought.csv file
def buy_product(product_name, buy_price, expiration_date,buy_date):

  exp_date = date.fromisoformat(expiration_date)

  product_name.lower()

  with open('bought.csv', 'a', newline='') as file:
    fieldnames = ['id',
                  'product_name',
                  'buy_price',
                    'buy_date',
                      'expiration_date']
    add = {
      'id' : bought_id(),
      'product_name' : product_name,
      'buy_price' : buy_price,
      'buy_date' : buy_date,
      'expiration_date' : exp_date
    }
    csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
    csv_writer.writerow(add)
    print(f'Product has been registered in bought.csv with the following purchase date: {buy_date}')


#to register sold products to the sold.csv file
def sell_product(bought_id, sell_price,sell_date):
    
    
    with open('sold.csv', 'r', newline='') as readfile:
       reader = csv.DictReader(readfile)
       bids = []

       for row in reader:
          bids.append(int(row['bought_id']))


    with open('sold.csv', 'a', newline='') as file:
      fieldnames = ['id',
                    'bought_id',
                    'sell_price',
                    'sell_date']
      add = {
        'id' : sold_id(),
        'bought_id' : bought_id,
        'sell_price' : sell_price,
        'sell_date' : sell_date}
      csv_writer = csv.DictWriter(file,fieldnames=fieldnames)

      if bought_id not in bids: 
        csv_writer.writerow(add)
        print(f"Product has been registered in sold.csv with todays date: {sell_date}")
      else:
         print("Bought id already in sold list please try another one")

#Exports a list of registered bought products to 'todays date'
def export_bought():
   
   path = Path.cwd() / "exports/bought_exports"
   path.mkdir(parents=True, exist_ok=True)


   with open('bought.csv', 'r', newline = '') as file:
      csv_reader = csv.DictReader(file)
      rows = list(csv_reader)

   file_name = 'bought_export_' + date_today()

   fpath = (path / file_name).with_suffix('.csv')   
   with fpath.open('w', newline='') as new_file:
      writer= csv.DictWriter(new_file, fieldnames = 
                              ['id',
                  'product_name',
                  'buy_price',
                    'buy_date',
                      'expiration_date'])
      
      writer.writeheader()
      for row in rows:
          if row['buy_date'] <= date_today():
            writer.writerow(row)
      print(f'Export has been created in the following folder : {path}. \nIf folder does not exist one will be made.')

#Export a list of registed sold products to 'todays date' 
def export_sold():
   
   path = Path.cwd() / "exports/sold_exports"
   path.mkdir(parents=True, exist_ok=True)

   with open('sold.csv', 'r', newline = '') as file:
      csv_reader = csv.DictReader(file)
      rows = list(csv_reader)

   file_name = 'sold_export_' + date_today()

   fpath = (path / file_name).with_suffix('.csv')   
   with fpath.open('w', newline='') as new_file:
      writer= csv.DictWriter(new_file, fieldnames = 
                              ['id',
                  'bought_id',
                  'sell_price',
                    'sell_date'])
      
      writer.writeheader()
      for row in rows:
          if row['sell_date'] <= date_today():
            writer.writerow(row)
      print(f'Export has been created in the following folder : {path}. \nIf folder does not exist one will be made.')

#exports a list of unsold products to 'todays date' 
def export_unsold():
    path = Path.cwd() / "exports/unsold_exports"
    path.mkdir(parents=True, exist_ok=True)


    with open('bought.csv', 'r', newline = '') as file:
      csv_reader = csv.DictReader(file)
      rows = list(csv_reader)

    file_name = 'unsold_export_' + date_today()

    fpath = (path / file_name).with_suffix('.csv')   
    with fpath.open('w', newline='') as new_file:
      writer= csv.DictWriter(new_file, fieldnames = 
                              ['id',
                  'product_name',
                  'buy_price',
                    'buy_date',
                      'expiration_date'])
      
      writer.writeheader()
      for row in rows:
          if row['buy_date'] <= date_today():
            if row['id'] not in sold_boughtid():
              writer.writerow(row)
      print(f'Export has been created in the following folder : {path}. \nIf folder does not exist one will be made.')

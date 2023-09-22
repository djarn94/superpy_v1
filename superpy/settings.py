import csv
from pathlib import *

#Returns current date (which can be changed by using change_date function).
def date_today():
   with open('time.csv', 'r') as file:
      next(file)
      reader = csv.reader(file)
      list = []
      for line in reader:
         list.append(line)

      return list[0][1]

def change_date(date):

      file = csv.reader(open('time.csv'))
      reader  = list(file)

      reader[1][1] = date
      
      writer = csv.writer(open('time.csv', 'w', newline=''))
      writer.writerows(reader)
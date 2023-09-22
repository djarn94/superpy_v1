# Imports
from argparse import *
import csv
from functions_write import *
from functions_read import *
from datetime import date
from settings import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    #Argparse superpy main
    parser = ArgumentParser(
        description="Welcome to the digital inventory tracker of Superpy",
        epilog="Have fun doing stuff!")

    #Menu holder for subparsers
    subparsers = parser.add_subparsers(dest="command")

    ##########################################################################################################################################
    #Bought sub_parser
    bought_parser = subparsers.add_parser(
        "bought", help='Use this function to register bought articles in the following order: 1.product name, 2.buy price, 3.expiration date')

    #bought options
    bought_parser.add_argument("product_name",type = str, help = 'product name as string')
    bought_parser.add_argument("buy_price",type = float, help ='fill in a number as float')
    bought_parser.add_argument("expiration_date",type = str, help = 'fill in expiration date in the following format : YYYY-MM-DD')
    ##########################################################################################################################################

    ##########################################################################################################################################
    #Sold sub_parser
    sold_parser = subparsers.add_parser(
        "sold", help='Use this function to register sold articles in the following order : 1.bought id, 2.sell price')


    #Sold options
    sold_parser.add_argument('bought_id',type = int, help = 'fill in the bought id here as int')
    sold_parser.add_argument('sell_price', type = float, help = 'fill in a number as float')

    ##########################################################################################################################################

    ##########################################################################################################################################
    #Inventory sub_parser
    inventory_parser = subparsers.add_parser(
        'inventory',
        help='Use this function to see the current inventory of the store')

    #Inventory options
    inventory_parser.add_argument('-now', help='show inventory of todays date')
    inventory_parser.add_argument('-bought', help= 'show list of all rows in bought.csv')
    inventory_parser.add_argument('-sold', help='show list of sold products')
    ##########################################################################################################################################

    profit_parser = subparsers.add_parser('profit',
                                          help = 'use this function to check expenses,revenue and profit of selected date (type in your desired date range in the following format : "YYYY-MM-DD")')
    
    profit_parser.add_argument('start_date',help='fill in start date in the following format : "YYYY-MM-DD"')
    profit_parser.add_argument('end_date',help='fill in the end date in the following format: "YYYY-MM-DD"')

    ##########################################################################################################################################
    graph_parser = subparsers.add_parser('graph', help='as example use: "graph 2023" to see profit per month over the year of 2023.')

    graph_parser.add_argument('year', help='enter a year in the following format : YYYY')
    ##########################################################################################################################################

    ##########################################################################################################################################
    #time_travel sub_parser
    time_travel_parser = subparsers.add_parser(
        'set_date',
        help=
        'use this function to set todays date to your choosing in the following format "YYYY-MM-DD" or use "today" to set date to current date.')

    #Time travel options
    time_travel_parser.add_argument('set', help='to set date to today or manual entered date.')
    ##########################################################################################################################################
    #Export sub_parser
    export_parser = subparsers.add_parser('export', help='use this function to export certain data use "export -h" for more help.')

    export_parser.add_argument('-bought', help='export a csv file with all bought products to todays date.')
    export_parser.add_argument('-sold', help='export a csv file with all sold products to todays date.')
    export_parser.add_argument('-unsold', help='see all unsold products to todays date.')
    ##########################################################################################################################################

    #Parse arguments
    #and if statements to decide the users input inside the CLI.
    args = parser.parse_args()

    if args.command == 'bought':
        buy_product(args.product_name.lower(), args.buy_price, args.expiration_date,date_today())
    elif args.command == 'sold':
        sell_product(args.bought_id, args.sell_price, date_today())
    elif args.command == 'inventory':
        if args.now == 'now':
            console.print(inventory_list())
        if args.bought == 'bought':
            console.print(bought_list())
        if args.sold == 'sold':
            console.print(sold_list())
    elif args.command == 'profit':
        console.print(profit(args.start_date, args.end_date))
    elif args.command == 'set_date':
            if args.set.lower() == 'today' :
                change_date(date.today())
            else:
                try:
                    date.fromisoformat(args.set)
                    change_date(args.set)
                except ValueError:
                    raise ValueError("Incorrect date format, please use the following format: YYYY-MM-DD")
    if args.command == 'export':
        if args.bought == 'bought':
            export_bought()
        if args.sold == 'sold':
            export_sold()
        if args.unsold == 'unsold':
            export_unsold()
    if args.command == 'graph':
        year_overview(args.year)
    else:
        pass      


if __name__ == "__main__":
    console = Console()
    main()
    print(f'use -h for a list of commands, current date is set to {date_today()}')
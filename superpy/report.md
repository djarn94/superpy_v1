SuperPy CLI application.

To register and keep track of your supermarket.

This app has been made in Python for most CLI's(I guess).
most important modules :

csv
argparse
DateTime
rich.Table & rich.Console

1.Register all bought products
2.Register all sold products
3.Keep track of current available inventory.
4.Show all bought products and if they are expired or sold.
5.Show all sold products.
6.Export bought or sold list.
7.time travel(set_date) to give you more options when to register bought or sold products and see certain reports of different time stamps.
8.Show Revenue, losses or profit made in certain date ranges or a graphical overview for selected year.

All above functions are descriped in the usage_guide.txt

The three most imporant functions of this CLI app:

------------------------------------------------------------------------------------------------

Function 7. is the backbone function of the app:
    def date_today():
    def change_date(date):
    This decided on which date you register,show rapports and export data and to what date it will show you information.
    This function is the core and most important to use correct to register and show rapports on the correct dates. 
    Also to make the correct exports.

    The date is saved to a csv file called : time.csv.
    This app is to tackle the problem to set your own today's date like your time traveling.
    Since I like it to be as flexible as possibe I choose to make it possible to type in your own custom date. 
    And to quickly set it to todays real date you can simply use set_date today.

4. function 4 is important to check which products are sold or expired in the bought.csv file
    def bought_list():
    and can be used multifunctional.
    Together with function 6.export which can also make a export file of all unsold products to todays date(set_date)
    def export_unsold(): 
    The export of unsold products is a handy side file to check what is not yet sold. And if desired this export can also be made of expired products! (not yet programmed into the CLI app.)

8. has two important functions:
    1. will show you the expenses,revenue and profit of a desired date range.
    def profit(start_date, end_date):
    2. shows a line graph which shows the profit or losses you have per month over the selected year.
    def year_overview(year):

    They are made to tackle the revenue,expenses and profit problem in a graph line(which can also be saved) and a report inside the cli app.

The rest of the functions are described in the usage_guide.txt

------------------------------------------------------------------------------------------------
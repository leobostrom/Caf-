import csv

def show_coffee_list():
    coffee_menu_list = []
    with open("kaffemeny.csv") as f:
        coffees = csv.reader(f)
        for coffee in coffees:
            print(coffee[0])
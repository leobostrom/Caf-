import csv
from kaffemeny_utils import show_coffee_list


class Menu:

    MAIN_MENU_TEXT = """
       -----------------
    -- Bosses coffee shop --
       ------------------

1: Show coffee menu
2: Order coffee
3: Show all orders
4: Quit menu
"""

    def user_input(self):
        return int(input("Enter your choice [1-4]: "))
    
    def choice(self, choice):
        if choice == 1:
            show_coffee_list()
        elif choice == 4:
            self.running = False
            print("Please come again")

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.choice(choice)

if __name__ == '__main__':
    menu = Menu()
    menu.menu_loop()
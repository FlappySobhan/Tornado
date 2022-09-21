from model.accounting import Accounting
from model.desk import Desk
from model.extra import Extra
from model.ingredient import Ingredient
from model.menu import Menu
from model.order import Order
from model.receipts import Receipts
from model.recipe import Recipe
from model.user import Users
from model.items import Items
from model.contact import Contact


def create_tables():
    Accounting.create_table_accounting()
    Desk.create_table_desk()
    Extra.create_table_extra()
    Ingredient.create_table_ingredient()
    Menu.create_table_menu()
    Order.create_table_order()
    Receipts.create_table_receipts()
    Recipe.create_table_recipe()
    Users.create_table_users()
    Items.create_table_items()
    Contact.create_table_contact()

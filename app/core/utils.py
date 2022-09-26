from model.configs import database
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
    db = database()
    with db:
        db.create_tables([Accounting, Desk, Extra, Ingredient,
                         Menu, Order, Receipts, Recipe, Users, Items, Contact])

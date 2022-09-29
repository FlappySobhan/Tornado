from models.base import database
from models.accounting import Accounting
from models.desk import Desk
from models.extra import Extra
from models.ingredient import Ingredient
from models.menu import Menu
from models.order import Order
from models.recipe import Recipe
from models.user import Users
from models.items import Items
from models.contact import Contact
from models.category import Category
from models.coupon import Coupon
from models.rule import Rule
from models.status import Status


def create_tables():
    db = database()
    with db:
        db.create_tables([Accounting, Desk, Extra, Ingredient, Coupon, Rule, Status,
                         Menu, Order, Recipe, Users, Items, Contact, Category])

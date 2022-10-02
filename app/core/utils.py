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
    """Create database tables based on defined models"""

    db = database()
    with db:
        db.create_tables([Accounting, Desk, Extra, Ingredient, Coupon, Rule, Status,
                         Menu, Order, Recipe, Users, Items, Contact, Category])


def generate_data():
    """Generate fake data for testing database tables and communications"""

    try:
        Category.select().get()
    except Exception:
        for _ in range(4):
            c = Category('hot drink', 'drink')
            c.save()

    try:
        Menu.select().get()
    except Exception:
        for i in range(1, 20):
            m = Menu('espresso', 1000, 0, '00:10:00', """Espresso is a concentrated form of coffee served in small,
                strong shots and is the base for many coffee drinks. it has less caffeine per serving.""",
                     '../static/img/A_small_cup_of_coffee.jpg', int(i/5) + 1)
            m.save()

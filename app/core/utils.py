from decouple import config
from datetime import datetime, timedelta
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
                     '../static/img/A_small_cup_of_coffee.jpg', int(i / 5) + 1)
            m.save()

    try:
        r = Rule.select().get()
    except Exception:
        for item in ['customer', 'employee', 'admin']:
            r = Rule(item)
            r.save()

    try:
        user = Users.select().get()
    except Exception:
        for i in range(1, 5):
            user = Users('jeff', 'bobs', '09123536842',
                         'iran-mashhad', config('SECURITY_PASS_TEST'), i, i, "customer")
            user.save()

    try:
        desk = Desk.select().get()
    except Exception:
        for i in range(1, 5):
            desk = Desk('strong', i, 2, 'free', 100)
            desk.save()

    try:
        status = Status.select().get()
    except Exception:
        for item in ['cooking', 'canceled', 'delivered', 'waiting']:
            status = Status(item)
            status.save()

    try:
        coupon = Coupon.select().get()
    except Exception:
        for i in range(1, 5):
            coupon = Coupon(f'{i}0x356', f"{i}00")
            coupon.save()

    try:
        order = Order.select().get()
    except Exception:
        for i in range(1, 5):
            order = Order('2002-10-10 14:23:16', '12345', 1000, i, i, i, i)
            order.save()

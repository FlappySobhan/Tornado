import pytest
from decouple import config
from werkzeug.security import check_password_hash

from models.coupon import Coupon
from models.rule import Rule
from models.status import Status
from models.user import Users
from models.recipe import Recipe
from models.order import Order
from models.extra import Extra
from models.menu import Menu
from models.desk import Desk
from models.category import Category
from models.accounting import Accounting
from models.ingredient import Ingredient
from models.contact import Contact
from core.exceptions import StructureError


# -------------------------------------------------------------------------------------------
#                                       TestCouponModel
# -------------------------------------------------------------------------------------------
class TestCouponModel:

    def test_coupon_success(self):
        self.p1 = Coupon('10x356', 850)
        assert self.p1.code == '10x356'
        assert self.p1.amount == 850

    @pytest.mark.parametrize('code, amount',
                             [
                                 ('', 850),
                                 ('10x356', ''),
                                 ('10x356', 'abc'),
                                 ('10x356', 1234567985210),
                             ]
                             )
    def test_coupon_raise(self, code, amount):
        pytest.raises(StructureError, Coupon, code, amount)


# -------------------------------------------------------------------------------------------
#                                       TestRuleModel
# -------------------------------------------------------------------------------------------
class TestRuleModel:

    def test_rule_success(self):
        self.p1 = Rule('customer')
        assert self.p1.rule == 'customer'

    @pytest.mark.parametrize('rule',
                             [
                                 (''),
                                 (1),
                                 ('abc'),
                                 ('user'),
                                 (' employee'),
                                 ('employee '),
                                 ('employee_id')
                             ]
                             )
    def test_rule_raise(self, rule):
        pytest.raises(StructureError, Rule, rule)


# -------------------------------------------------------------------------------------------
#                                       TestStatusModel
# -------------------------------------------------------------------------------------------
class TestStatusModel:

    def test_status_success(self):
        self.p1 = Status('cooking')
        assert self.p1.status == 'cooking'

    @pytest.mark.parametrize('status',
                             [
                                 (''),
                                 (1),
                                 ('abc'),
                                 ('user'),
                                 (' cooking'),
                                 ('cooking '),
                                 ('cooking_id')
                             ]
                             )
    def test_status_raise(self, status):
        pytest.raises(StructureError, Status, status)


# -------------------------------------------------------------------------------------------
#                                       TestUserModel
# -------------------------------------------------------------------------------------------
class TestUserModel:

    def test_user_success(self):
        self.p1 = Users('jeff', 'bobs', '09123536842',
                        'iran-mashhad', config('SECURITY_PASS_TEST'), 100, 55, 1)
        assert self.p1.name == 'jeff'
        assert self.p1.family == 'bobs'
        assert self.p1.phone == '09123536842'
        assert self.p1.address == 'iran-mashhad'
        assert check_password_hash(self.p1.password, config('SECURITY_PASS_TEST'))
        assert self.p1.balance == 100
        assert self.p1.subscription == 55

    @pytest.mark.parametrize('name, family, phone, address, password, balance, subscription, rule',
                             [
                                 ('', 'yaghoubi', '09123536842',
                                  'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('a', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('12345', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', '', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', 'a', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', '12345', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', 'yaghoubi', 'bad',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '12345',
                                     'iran-mashhad', '123!qwerQW', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     '', '123!qwerQW', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', 'abc', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '!@#$', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', 'abcdefgh', 0, 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 'bad', 100, 1),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 'bad', 1)
                             ]
                             )
    def test_user_raise(self, name, family, phone, address, password, balance, subscription, rule):
        pytest.raises(StructureError, Users, name, family, phone,
                      address, password, balance, subscription, rule)


# -------------------------------------------------------------------------------------------
#                                       TestExtraModel
# -------------------------------------------------------------------------------------------
class TestExtraModel:

    def test_extra_success(self):
        self.p1 = Extra('example@me.com', '09123536842',
                        'address', 'nothing', 1)
        assert self.p1.email == 'example@me.com'
        assert self.p1.phone == '09123536842'
        assert self.p1.address == 'address'
        assert self.p1.info == 'nothing'

    @pytest.mark.parametrize('email, phone, address, info, user',
                             [
                                 ('example.com', '09123536842',
                                  'address', 'nothing', 1),
                                 ('example@me', '09123536842',
                                  'address', 'nothing', 1),
                                 ('@me.com', '09123536842',
                                  'address', 'nothing', 1),
                                 ('.com', '09123536842', 'address', 'nothing', 1),
                                 ('example@.com@.com', '09123536842',
                                     'address', 'nothing', 1),
                                 ('.com', '123', 'address', 'nothing', 1),
                                 ('.com', 'abc', 'address', 'nothing', 1),
                                 ('.com', '09123536842', '', 'nothing', 1)
                             ]
                             )
    def test_extra_raise(self, email, phone, address, info, user):
        pytest.raises(StructureError, Extra, email, phone, address, info, user)


# -------------------------------------------------------------------------------------------
#                                       TestRecipeModel
# -------------------------------------------------------------------------------------------
class TestRecipeModel:

    def test_recipe_success(self):
        self.p1 = Recipe(100, 1, 1)
        assert self.p1.quantity == 100

    @pytest.mark.parametrize('quantity, menu, ingredient',
                             [
                                 ('', 1, 1),
                                 ('abcd', 1, 1),
                                 (12345678901, 1, 1),
                                 (1.12345678, 1, 1)
                             ]
                             )
    def test_recipe_raise(self, quantity, menu, ingredient):
        pytest.raises(StructureError, Recipe, quantity, menu, ingredient)


# -------------------------------------------------------------------------------------------
#                                       TestOrderModel
# -------------------------------------------------------------------------------------------
class TestOrderModel:

    def test_order_success(self):
        self.p1 = Order('2002-10-10 14:23:16', 55, 10_000, 1, 1, 1, 1)
        assert self.p1.deliver == '2002-10-10 14:23:16'
        assert self.p1.code == 55
        assert self.p1.cost == 10_000

    @pytest.mark.parametrize('deliver, code, cost, user, desk, status, coupon',
                             [
                                 ('', 100, 10_000, 1, 1, 1, 1),
                                 (1234, 100, 10_000, 1, 1, 1, 1),
                                 ('abc', 100, 10_000, 1, 1, 1, 1),
                                 ('2002-10-10 14:23:16', 'abc', 10_000, 1, 1, 1, 1),
                                 ('2002-10-10 14:23:16', 100, 12345678909, 1, 1, 1, 1),
                             ]
                             )
    def test_order_raise(self, deliver, code, cost, user, desk, status, coupon):
        pytest.raises(StructureError, Order,
                      deliver, code, cost, user, desk, status, coupon)


# -------------------------------------------------------------------------------------------
#                                       TestMenuModel
# -------------------------------------------------------------------------------------------
class TestMenuModel:

    def test_menu_success(self):
        self.p1 = Menu('coffee', 10_000, 1_000, '00:10:00', 1)
        assert self.p1.name == 'coffee'
        assert self.p1.price == 10_000
        assert self.p1.discount == 1_000
        assert self.p1.preparation == '00:10:00'

    @pytest.mark.parametrize('name, price, discount, preparation, category',
                             [
                                 ('', 10_000, 1_000, '00:10:00', 1),
                                 (123, 10_000, 1_000, '00:10:00', 1),
                                 ('coffee', 'abc', 1_000, '00:10:00', 1),
                                 ('coffee', 10_000, .12345678, '00:10:00', 1),
                                 ('coffee', 10_000, 1_000, 'abc', 1),
                                 ('coffee', 10_000, 1_000, 123, 1),
                                 ('coffee', 10_000, 1_000, '', 1),
                                 ('coffee', 10_000, 1_000, '00=10=00', 1),
                                 ('coffee', 10_000, 1_000, '10=00', 1),
                                 ('coffee', 10_000, 1_000, '00:10=00', 1),
                                 ('coffee', 10_000, 1_000, '00:10:00:00', 1)
                             ]
                             )
    def test_menu_raise(self, name, price, discount, preparation, category):
        pytest.raises(StructureError, Menu, name, price, discount, preparation, category)


# -------------------------------------------------------------------------------------------
#                                       TestIngredientModel
# -------------------------------------------------------------------------------------------
class TestIngredientModel:

    def test_ingredient_success(self):
        self.p1 = Ingredient('milk', 'kilo',  10_000)
        assert self.p1.name == 'milk'
        assert self.p1.unit == 'kilo'
        assert self.p1.cost == 10_000

    @pytest.mark.parametrize('name, unit, cost',
                             [
                                 ('', 'kilo',  10_000),
                                 (124, 'kilo',  10_000),
                                 ('a', 'kilo', 10_000),
                                 ('milk', '', 10_000),
                                 ('milk', 'kilo', ''),
                                 ('milk', 'kilo', 'abc')
                             ]
                             )
    def test_ingredient_raise(self, name, unit, cost):
        pytest.raises(StructureError, Ingredient, name, unit, cost)


# -------------------------------------------------------------------------------------------
#                                       TestDeskModel
# -------------------------------------------------------------------------------------------
class TestDeskModel:

    def test_desk_success(self):
        self.p1 = Desk('strong', 1, 2, 'free', 100)
        assert self.p1.name == 'strong'
        assert self.p1.number == 1
        assert self.p1.capacity == 2
        assert self.p1.status == 'free'
        assert self.p1.cost == 100

    @pytest.mark.parametrize('name, number, capacity, status, cost',
                             [
                                 (123, '', 2, 'free', 100),
                                 ('', '', 2, 'free', 100),
                                 ('strong', '', 2, 'free', 100),
                                 ('strong', 'abc', 2, 'free', 100),
                                 ('strong', 12345, 2, 'free', 100),
                                 ('strong', 1, '', 'free', 100),
                                 ('strong', 1, 'a', 'free', 100),
                                 ('strong', 1, 12345, 'free', 100),
                                 ('strong', 1, 2, '', 100),
                                 ('strong', 1, 2, 'free', 'a')
                             ]
                             )
    def test_desk_raise(self, name, number, capacity, status, cost):
        pytest.raises(StructureError, Desk, name,
                      number, capacity, status, cost)


# -------------------------------------------------------------------------------------------
#                                       TestAccountingModel
# -------------------------------------------------------------------------------------------
class TestAccountingModel:

    def test_accounting_success(self):
        self.p1 = Accounting(1_000, 'somethings', 1)
        assert self.p1.profit == 1_000
        assert self.p1.description == 'somethings'

    @pytest.mark.parametrize('profit, description, order',
                             [
                                 ('', 'somethings', 1),
                                 (1_000, '', 1),
                                 ('abc', 'somethings', 1),
                                 ('abc', 'somethings', ''),
                                 ('abc', 'somethings', 'abc'),
                             ]
                             )
    def test_accounting_raise(self, profit, description, order):
        pytest.raises(StructureError, Accounting, profit, description, order)


# -------------------------------------------------------------------------------------------
#                                       TestContactModel
# -------------------------------------------------------------------------------------------
class TestContactModel:

    def test_contact_success(self):
        self.p1 = Contact('strong', 'test@gmail.com', 'hello', 1)
        assert self.p1.name == 'strong'
        assert self.p1.email == 'test@gmail.com'
        assert self.p1.message == 'hello'

    @pytest.mark.parametrize('name, email, message, user',
                             [
                                 ('', 'test@gmail.com', 'hello', 1),
                                 ('strong', '@gmail.com', 'hello', 1),
                                 ('strong', '@gmail.com', 'hello', 1),
                                 ('strong', '@com', 'hello', 1),
                                 ('strong', '@', 'hello', 1),
                                 ('strong', 'test@gmail.com', '', 1),
                                 (123, 'test@gmail.com', 'hello', 1)
                             ]
                             )
    def test_contact_raise(self, name, email, message, user):
        pytest.raises(StructureError, Contact, name, email, message, user)


# -------------------------------------------------------------------------------------------
#                                       TestCategoryModel
# -------------------------------------------------------------------------------------------
class TestCategoryModel:

    def test_coupon_success(self):
        self.p1 = Category('drink', 'coffee', 1)
        assert self.p1.name == 'drink'
        assert self.p1.parent == 'coffee'

    @pytest.mark.parametrize('name, parent, relation',
                             [
                                 ('', 'test', ''),
                                 ('test', '', '')
                             ]
                             )
    def test_coupon_raise(self, name, parent, relation):
        pytest.raises(StructureError, Category, name, parent, relation)

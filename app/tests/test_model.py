import pytest
from decouple import config

from model.user import Users
from model.recipe import Recipe
from model.receipts import Receipts
from model.order import Order
from model.extra import Extra
from model.menu import Menu
from model.desk import Desk
from model.accounting import Accounting
from model.ingredient import Ingredient
from model.contact import Contact
from core.exceptions import StructureError


class TestUserModel:

    def test_user_success(self):
        self.p1 = Users('jeff', 'bobs', '09123536842',
                        'iran-mashhad', config('SECURITY_PASS_TEST'), 100, 100)
        assert self.p1.name == 'jeff'
        assert self.p1.family == 'bobs'
        assert self.p1.phone == '09123536842'
        assert self.p1.address == 'iran-mashhad'
        assert self.p1.password == config('SECURITY_PASS_TEST')
        assert self.p1.balance == 100
        assert self.p1.subscription == 100

    @pytest.mark.parametrize('name, family, phone, address, password, balance, subscription',
                             [
                                 ('', 'yaghoubi', '09123536842',
                                  'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('a', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('12345', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', '', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', 'a', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', '12345', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', 'yaghoubi', '',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', 'yaghoubi', 'bad',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', 'yaghoubi', '12345',
                                     'iran-mashhad', '123!qwerQW', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     '', '123!qwerQW', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', 'abc', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '!@#$', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', 'abcdefgh', 0, 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 'bad', 100),
                                 ('jeff', 'yaghoubi', '09123536842',
                                     'iran-mashhad', '123!qwerQW', 0, 'bad')
                             ]
                             )
    def test_user_raise(self, name, family, phone, address, password, balance, subscription):
        pytest.raises(StructureError, Users, name, family, phone,
                      address, password, balance, subscription)


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


class TestRecipeModel:

    def test_recipe_success(self):
        self.p1 = Recipe(100, 1, 1)
        assert self.p1.cost == 100

    @pytest.mark.parametrize('cost, menu, ingredient',
                             [
                                 ('', 1, 1),
                                 ('abcd', 1, 1),
                                 (12345678901, 1, 1),
                                 (1.12345678, 1, 1)
                             ]
                             )
    def test_recipe_raise(self, cost, menu, ingredient):
        pytest.raises(StructureError, Recipe, cost, menu, ingredient)


class TestReceiptsModel:

    def test_receipts_success(self):
        self.p1 = Receipts(100, '2002-10-10 14:23:16', 100, 'alex bob', 2, 1)
        assert self.p1.cost == 100
        assert self.p1.delivery == '2002-10-10 14:23:16'
        assert self.p1.code == 100
        assert self.p1.customer == 'alex bob'
        assert self.p1.desk == 2

    @pytest.mark.parametrize('cost, delivery, code, customer, desk, order',
                             [
                                 ('abc', '2002-10-10 14:23:16',
                                  100, 'alex bob', 1, 1),
                                 (12345678902, '2002-10-10 14:23:16',
                                  100, 'alex bob', 1, 1),
                                 (1.12345678, '2002-10-10 14:23:16',
                                     100, 'alex bob', 1, 1),
                                 (100, '', 100, 'alex bob', 1, 1),
                                 (100, '123', 100, 'alex bob', 1, 1),
                                 (100, '2002-10-10 14:23:16',
                                  'abc', 'alex bob', 1, 1),
                                 (100, '2002-10-10 14:23:16', '', 'alex bob', 1, 1),
                                 (100, '2002-10-10 14:23:16',
                                     1234567890, 'alex bob', 1, 1),
                                 (100, '2002-10-10 14:23:16', 100, '', 1, 1),
                                 (100, '2002-10-10 14:23:16', 100, 123, 1, 1),
                                 (100, '2002-10-10 14:23:16',
                                     100, 'alex bob', 12345, 1),
                                 (100, '2002-10-10 14:23:16',
                                  100, 'alex bob', '', 1),
                             ]
                             )
    def test_receipts_raise(self, cost, delivery, code, customer, desk, order):
        pytest.raises(StructureError, Receipts, cost,
                      delivery, code, customer, desk, order)


class TestOrderModel:

    def test_order_success(self):
        self.p1 = Order('waiting', '2002-10-10 14:23:16', '2002-10-10 14:23:16', 100, 10_000, 1, 1)
        assert self.p1.status == 'waiting'
        assert self.p1.register == '2002-10-10 14:23:16'
        assert self.p1.deliver == '2002-10-10 14:23:16'
        assert self.p1.code == 100
        assert self.p1.cost == 10_000

    @pytest.mark.parametrize('status, register, deliver, code, cost, user, desk',
                             [
                                 ('', '2002-10-10 14:23:16',
                                  '2002-10-10 14:23:16', 100, 10_000, 1, 1),
                                 ('waiting', 1234, '2002-10-10 14:23:16',
                                  100, 10_000, 1, 1),
                                 ('waiting', '2002-10-10 14:23:16',
                                  1234, 100, 10_000, 1, 1),
                                 ('waiting', '2002-10-10 14:23:16',
                                  '2002-10-10 14:23:16', 'abc', 10_000, 1, 1),
                                 ('waiting', '2002-10-10 14:23:16',
                                  '2002-10-10 14:23:16', 'abc', '', 1, 1),
                                 ('waiting', '2002-10-10 14:23:16',
                                  '2002-10-10 14:23:16', 'abc', 123456789, 1, 1),
                             ]
                             )
    def test_order_raise(self, status, register, deliver, code, cost, user, desk):
        pytest.raises(StructureError, Order, status, register,
                      deliver, code, cost, user, desk)


class TestMenuModel:

    def test_menu_success(self):
        self.p1 = Menu('coffee', 10_000, 1_000,
                       'drink', 'breakfast', '00:10:00')
        assert self.p1.name == 'coffee'
        assert self.p1.price == 10_000
        assert self.p1.discount == 1_000
        assert self.p1.category == 'drink'
        assert self.p1.meal == 'breakfast'
        assert self.p1.preparation == '00:10:00'

    @pytest.mark.parametrize('name, price, discount, category, meal, preparation',
                             [
                                 ('', 10_000, 1_000, 'drink',
                                  'breakfast', '00:10:00'),
                                 (123, 10_000, 1_000, 'drink',
                                     'breakfast', '00:10:00'),
                                 ('coffee', 'abc', 1_000, 'drink',
                                     'breakfast', '00:10:00'),
                                 ('coffee', 10_000, .12345678,
                                     'drink', 'breakfast', '00:10:00'),
                                 ('coffee', 10_000, 1_000, '',
                                     'breakfast', '00:10:00'),
                                 ('coffee', 10_000, 1_000, 'drink', '', 'abc'),
                                 ('coffee', 10_000, 1_000, 'drink', '', 123),
                                 ('coffee', 10_000, 1_000, 'drink', '', ''),
                                 ('coffee', 10_000, 1_000,
                                  'drink', '', '00=10=00'),
                                 ('coffee', 10_000, 1_000, 'drink', '', '10=00'),
                                 ('coffee', 10_000, 1_000,
                                  'drink', '', '00:10=00'),
                                 ('coffee', 10_000, 1_000,
                                     'drink', '', '00:10:00:00')
                             ]
                             )
    def test_menu_raise(self, name, price, discount, category, meal, preparation):
        pytest.raises(StructureError, Menu, name,
                      price, discount, category, meal, preparation)


class TestIngredientModel:

    def test_ingredient_success(self):
        self.p1 = Ingredient('milk', 100, 'kilo', 'dairy', 10_000)
        assert self.p1.name == 'milk'
        assert self.p1.quantity == 100
        assert self.p1.unit == 'kilo'
        assert self.p1.category == 'dairy'
        assert self.p1.cost == 10_000

    @pytest.mark.parametrize('name, quantity, unit, category, cost',
                             [
                                 ('', 100, 'kilo', 'dairy', 10_000),
                                 (124, 100, 'kilo', 'dairy', 10_000),
                                 ('a', 100, 'kilo', 'dairy', 10_000),
                                 ('milk', 'a', 'kilo', 'dairy', 10_000),
                                 ('milk', '', 'kilo', 'dairy', 10_000),
                                 ('milk', 100, '', 'dairy', 10_000),
                                 ('milk', 100, 'kilo', '', 10_000),
                                 ('milk', 100, 'kilo', 'dairy', 'abc')
                             ]
                             )
    def test_ingredient_raise(self, name, quantity, unit, category, cost):
        pytest.raises(StructureError, Ingredient, name,
                      quantity, unit, category, cost)


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


class TestContactModel:

    def test_contact_success(self):
        self.p1 = Contact('strong', 'test@gmail.com', 'hello')
        assert self.p1.name == 'strong'
        assert self.p1.email == 'test@gmail.com'
        assert self.p1.message == 'hello'

    @pytest.mark.parametrize('name, email, message',
                             [
                                 ('', 'test@gmail.com', 'hello'),
                                 ('strong', '@gmail.com', 'hello'),
                                 ('strong', '@gmail.com', 'hello'),
                                 ('strong', '@com', 'hello'),
                                 ('strong', '@', 'hello'),
                                 ('strong', 'test@gmail.com', ''),
                                 (123, 'test@gmail.com', 'hello')
                             ]
                             )
    def test_contact_raise(self, name, email, message):
        pytest.raises(StructureError, Contact, name, email, message)

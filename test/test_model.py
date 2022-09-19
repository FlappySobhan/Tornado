import pytest

# from model.user import Users
# from model.recipe import Recipe
# from model.receipts import Receipts
# from model.order import Order
# from model.extra import Extra
# from model.menu import Menu
from model.desk import Desk
from model.accounting import Accounting
# from model.ingredient import Ingredient
from exceptions import *


# class TestUserModel:

#     def test_user_success(self):
#         self.p1 = Users('jeff', 'yaghoubi', '09123536842',
#                         'iran-mashhad', '123!qwerQW', 0, 100)
#         assert self.p1.name == 'jafar'
#         assert self.p1.family == 'Yaghoubi'
#         assert self.p1.phone == '09123536842'
#         assert self.p1.address == 'iran-mashhad'
#         assert self.p1.password == '123!qwerQW'
#         assert self.p1.balance == 0
#         assert self.p1.subscription == 100

#     @pytest.mark.parametrize('name, family, phone, address, password, balance, subscription',
#                              [
#                                  ('', 'yaghoubi', '09123536842',
#                                   'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('a', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('12345', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', '', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', 'a', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', '12345', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', 'yaghoubi', '',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', 'yaghoubi', 'bad',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', 'yaghoubi', '12345',
#                                      'iran-mashhad', '123!qwerQW', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      '', '123!qwerQW', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '123', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', 'abc', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '!@#$', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', 'abcdefgh', 0, 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 'bad', 100),
#                                  ('jeff', 'yaghoubi', '09123536842',
#                                      'iran-mashhad', '123!qwerQW', 0, 'bad')
#                              ]
#                             )
                            
#     def test_user_raise(self, name, family, phone, address, password, balance, subscription):
#         pytest.raises(StructureError, Users, name, family, phone,
#                       address, password, balance, subscription)


# class TestExtraModel:

#     def test_extra_success(self):
#         self.p1 = Extra('example@me.com', '09123536842', 'address', 'nothing')
#         assert self.p1.email == 'example@me.com'
#         assert self.p1.phone == '09123536842'
#         assert self.p1.address == 'address'
#         assert self.p1.info == 'nothing'

#     @pytest.mark.parametrize('email, phone, address, info',
#                              [
#                                  ('example.com', '09123536842',
#                                   'address', 'nothing'),
#                                  ('example@me', '09123536842',
#                                   'address', 'nothing'),
#                                  ('@me.com', '09123536842', 'address', 'nothing'),
#                                  ('.com', '09123536842', 'address', 'nothing'),
#                                  ('example@.com@.com', '09123536842',
#                                      'address', 'nothing'),
#                                  ('.com', '123', 'address', 'nothing'),
#                                  ('.com', 'abc', 'address', 'nothing'),
#                                  ('.com', '09123536842', '', 'nothing')
#                              ]
#                             )

#     def test_extra_raise(email, phone, address, info):
#         pytest.raises(StructureError, Extra, email,
#                       phone, address, info)


# class TestRecipeModel:

#     def test_recipe_success(self):
#         self.p1 = Recipe(100)
#         assert self.p1.cost == 100

#     @pytest.mark.parametrize('cost',
#                              [
#                                  (''),
#                                  ('abcd'),
#                                  (.1234),
#                                  (1.12345678)
#                              ]
#                             )

#     def test_recipe_raise(self, cost):
#         pytest.raises(StructureError, Recipe, cost)


# class TestReceiptsModel:

#     def test_receipts_success(self):
#         self.p1 = Receipts(100, '2002-10-10 14:23:16', 100, 'alex bob', 1)
#         assert self.p1.cost == 100
#         assert self.p1.delivery == '2002-10-10 14:23:16'
#         assert self.p1.code == 100
#         assert self.p1.customer == 'alex bob'
#         assert self.p1.desk == 1

#     @pytest.mark.parametrize('cost, delivery, code, customer, desk',
#                              [
#                                  ('abc', '2002-10-10 14:23:16', 100, 'alex bob', 1),
#                                  (.123, '2002-10-10 14:23:16', 100, 'alex bob', 1),
#                                  (1.12345678, '2002-10-10 14:23:16',
#                                      100, 'alex bob', 1),
#                                  (100, '', 100, 'alex bob', 1),
#                                  (100, '123', 100, 'alex bob', 1),
#                                  (100, '2002-10-10 14:23:16', 'abc', 'alex bob', 1),
#                                  (100, '2002-10-10 14:23:16', '', 'alex bob', 1),
#                                  (100, '2002-10-10 14:23:16',
#                                      1234567890, 'alex bob', 1),
#                                  (100, '2002-10-10 14:23:16', 100, '', 1),
#                                  (100, '2002-10-10 14:23:16', 100, 123, 1),
#                                  (100, '2002-10-10 14:23:16',
#                                      100, 'alex bob', 12345),
#                                  (100, '2002-10-10 14:23:16', 100, 'alex bob', ''),
#                              ]
#                             )

#     def test_receipts_raise(self, cost, delivery, code, customer, desk):
#         pytest.raises(StructureError, Receipts, cost,
#                       delivery, code, customer, desk)


# class TestOrderModel:

#     def test_order_success(self):
#         self.p1 = Order('waiting', '2002-10-10 14:23:16',
#                         '2002-10-10 14:23:16', 100, 10_000)
#         assert self.p1.status == 'waiting'
#         assert self.p1.register == '2002-10-10 14:23:16'
#         assert self.p1.deliver == '2002-10-10 14:23:16'
#         assert self.p1.code == 100
#         assert self.p1.cost == 10_000

#     @pytest.mark.parametrize('status, register, deliver, code, cost',
#                              [
#                                  ('', '2002-10-10 14:23:16',
#                                   '2002-10-10 14:23:16', 100, 10_000),
#                                  ('waiting', 1234, '2002-10-10 14:23:16', 100, 10_000),
#                                  ('waiting', '2002-10-10 14:23:16',
#                                   1234, 100, 10_000),
#                                  ('waiting', '2002-10-10 14:23:16',
#                                      '2002-10-10 14:23:16', 'abc', 10_000),
#                                  ('waiting', '2002-10-10 14:23:16',
#                                   '2002-10-10 14:23:16', 'abc', ''),
#                                  ('waiting', '2002-10-10 14:23:16',
#                                   '2002-10-10 14:23:16', 'abc', 123456789),
#                              ]
#                              )
#     def test_order_raise(status, register, deliver, code, cost):
#         pytest.raises(StructureError, Order, status,
#                       register, deliver, code, cost)


# class TestMenuModel:

#     def test_menu_success(self):
#         self.p1 = Menu('coffee', 10_000, 1_000,
#                        'drink', 'breakfast', '00:10:00')
#         assert self.p1.name == 'coffee'
#         assert self.p1.price == 10_000
#         assert self.p1.discount == 1_000
#         assert self.p1.category == 'drink'
#         assert self.p1.meal == 'breakfast'
#         assert self.p1.preparation == '00:10:00'

#     @pytest.mark.parametrize('name, price, discount, category, meal, preparation',
#                              [
#                                  ('', 10_000, 1_000, 'drink',
#                                   'breakfast', '00:10:00'),
#                                  (123, 10_000, 1_000, 'drink',
#                                      'breakfast', '00:10:00'),
#                                  ('coffee', 'abc', 1_000, 'drink',
#                                      'breakfast', '00:10:00'),
#                                  ('coffee', 10_000, .12345678,
#                                      'drink', 'breakfast', '00:10:00'),
#                                  ('coffee', 10_000, 1_000, '',
#                                      'breakfast', '00:10:00'),
#                                  ('coffee', 10_000, 1_000, 'drink', '', 'abc'),
#                                  ('coffee', 10_000, 1_000, 'drink', '', 123),
#                                  ('coffee', 10_000, 1_000, 'drink', '', ''),
#                                  ('coffee', 10_000, 1_000,
#                                   'drink', '', '00=10=00'),
#                                  ('coffee', 10_000, 1_000, 'drink', '', '10=00'),
#                                  ('coffee', 10_000, 1_000,
#                                   'drink', '', '00:10=00'),
#                                  ('coffee', 10_000, 1_000,
#                                      'drink', '', '00:10:00:00')
#                              ]
#                             )

#     def test_menu_raise(name, price, discount, category, meal, preparation):
#         pytest.raises(StructureError, Menu, name,
#                       price, discount, category, meal, preparation)


# class TestIngredientModel:

#     def test_ingredient_success(self):
#         self.p1 = Ingredient('milk', 100, 'kilo', 'dairy', 10_000)
#         assert self.p1.name == 'milk'
#         assert self.p1.quantity == 100
#         assert self.p1.unit == 'kilo'
#         assert self.p1.category == 'dairy'
#         assert self.p1.cost == 10_000

#     @pytest.mark.parametrize('name, quantity, unit, category, cost',
#                              [
#                                  ('', 100, 'kilo', 'dairy', 10_000),
#                                  (124, 100, 'kilo', 'dairy', 10_000),
#                                  ('a', 100, 'kilo', 'dairy', 10_000),
#                                  ('milk', 'a', 'kilo', 'dairy', 10_000),
#                                  ('milk', '', 'kilo', 'dairy', 10_000),
#                                  ('milk', 100, '', 'dairy', 10_000),
#                                  ('milk', 100, 'kilo', '', 10_000),
#                                  ('milk', 100, 'kilo', 'dairy', 'abc')
#                              ]
#                             )

#     def test_ingredient_raise(name, quantity, unit, category, cost):
#         pytest.raises(StructureError, Ingredient, name,
#                       quantity, unit, category, cost)


class TestDeskModel:

    def test_desk_success(self):
        self.p1 = Desk(1, 2, 'free', 100)
        assert self.p1.number == 1
        assert self.p1.capacity == 2
        assert self.p1.status == 'free'
        assert self.p1.cost == 100

    @pytest.mark.parametrize('number, capacity, status, cost',
                             [
                                 ('', 2, 'free', 100),
                                #  ('abc', 2, 'free', 100),
                                #  (12345, 2, 'free', 100),
                                #  (1, '', 'free', 100),
                                #  (1, 'a', 'free', 100),
                                #  (1, 12345, 'free', 100),
                                #  (1, 2, '', 100),
                                #  (1, 2, 'free', 'a')
                             ]
                            )

    def test_desk_raise(self, number, capacity, status, cost):
        pytest.raises(StructureError, Desk, number, capacity, status, cost)


class TestAccountingModel:

    def test_accounting_success(self):
        self.p1 = Accounting(1_000, 'somethings')
        assert self.p1.profit == 1_000
        assert self.p1.description == 'somethings'

    @pytest.mark.parametrize('profit, description',
                             [
                                 ('', 'somethings'),
                                 (1_000, ''),
                                 ('abc', 'somethings')
                             ]
                            )

    def test_accounting_raise(self, profit, description):
        pytest.raises(StructureError, Accounting, profit, description)

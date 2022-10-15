from core.router import Route, Handler
from views.home import home
from views.menu import menu
from views.order import new_order
from views.order import show_order
from views.order import delete_order
from views.error import not_found
from views.contact import contact, contact_us
from views.signup import signup
from views.login import login
from views.dashboard import dashboard, order_history, logout

routes = [
    Route("/", endpoint=None, view_func=home),
    Route("/menu/", endpoint=None, view_func=menu),
    Route("/order/new/{table_id}", endpoint=None,
          view_func=new_order, methods=['POST']),
    Route("/order/show/{table_id}", endpoint=None, view_func=show_order),
    Route("/order/delete/{table_id}", endpoint=None,
          view_func=delete_order, methods=['DELETE']),
    Route("/contact_us/", endpoint=None, view_func=contact_us, methods=['GET', 'POST']),
    Route("/contact/", endpoint=None, view_func=contact, methods=['GET', 'POST']),
    Route("/signup/", endpoint=None, view_func=signup, methods=['GET', 'POST']),
    Route("/login/", endpoint=None, view_func=login, methods=['GET', 'POST']),
    Route("/dashboard/", endpoint=None, view_func=dashboard, methods=['GET', 'POST']),
    Route("/order_history/", endpoint=None, view_func=order_history, methods=['GET', 'POST']),
    Route("/logout/", endpoint=None, view_func=order_history, methods=['GET', 'POST']),
    # Route("/dashboard/edit_user", endpoint=None, view_func=edit_user_show, methods=['GET', 'POST']),
    # Handlers:
    Handler(404, not_found)
]

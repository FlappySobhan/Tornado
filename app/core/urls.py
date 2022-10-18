from core.router import Route, Handler
from views.home import home
from views.menu import menu
from views.order import new_order
from views.order import show_order
from views.order import delete_order
from views.error import not_found
from views.contact import contact
from views.signup import signup
from views.login import login
from views.dashboard import dashboard, order_history, logout, change_password
from views.employee import dashboard_employee, dashboard_admin

routes = [
    Route("/", view_func=home),
    Route("/menu/", view_func=menu),
    Route("/order/new/{table_id}", view_func=new_order, methods=['POST']),
    Route("/order/show/{table_id}", view_func=show_order),
    Route("/order/delete/{table_id}", view_func=delete_order, methods=['DELETE']),
    Route("/contact/", view_func=contact, methods=['GET', 'POST']),
    Route("/signup/", view_func=signup, methods=['GET', 'POST']),
    Route("/login/", view_func=login, methods=['GET', 'POST']),
    Route("/dashboard/", view_func=dashboard, methods=['GET', 'POST']),
    Route("/order_history/", view_func=order_history, methods=['GET', 'POST']),
    Route("/logout/", view_func=logout, methods=['GET', 'POST']),
    Route("/change_password/", view_func=change_password, methods=['GET', 'POST']),
    Route("/employee_panel/", view_func=dashboard_employee, methods=['GET', 'POST']),
    Route("/employee_admin/", view_func=dashboard_admin, methods=['GET', 'POST']),
    # Handlers:
    Handler(404, not_found)
]

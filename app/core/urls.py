from core.router import Route, Handler
from views.home import home
from views.menu import menu
from views.order import new_order
from views.order import show_order
from views.order import delete_order
from views.error import not_found

routes = [
    Route("/", endpoint=None, view_func=home),
    Route("/menu", endpoint=None, view_func=menu),
    Route("/order/new/{table_id}", endpoint=None,
          view_func=new_order, methods=['POST']),
    Route("/order/show/{table_id}", endpoint=None, view_func=show_order),
    Route("/order/delete/{table_id}", endpoint=None,
          view_func=delete_order, methods=['DELETE']),


    # Handlers:
    Handler(404, not_found)
]

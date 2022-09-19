from views.utils import Route, Handler
from views.views import home
from views.views import menu
from views.views import new_order
from views.views import show_order
from views.views import delete_order
from views.views import not_found

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

from views.utils import Route, Handler
from views.views import *

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

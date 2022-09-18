from views.utils import Route, Handler
import views.views

routes = [
    Route("/", endpoint=None, view_func=views.home),
    Route("/menu", endpoint=None, view_func=views.menu),
    Route("/order/new/{table_id}", endpoint=None,
          view_func=views.new_order, methods=['POST']),
    Route("/order/show/{table_id}", endpoint=None, view_func=views.show_order),
    Route("/order/delete/{table_id}", endpoint=None,
          view_func=views.delete_order, methods=['DELETE']),


    # Handlers:
    Handler(404, views.not_found)
]

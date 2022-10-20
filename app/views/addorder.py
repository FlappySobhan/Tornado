from flask import request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timedelta

from models.order import Order
from models.items import Items
from models.menu import Menu
from models.desk import Desk


@login_required
def add_order():
    if request.method == 'POST':
        order_data = request.json
        menu_items = []
        for item in order_data:
            menu_item = Menu.select().where(Menu.name == item['name']).first()
            menu_items = list(map(lambda x: menu_item, range(item['count'])))

        added_time = sum(menu_item.preparation.minute for menu_item in menu_items)
        deliver_time = datetime.now() + timedelta(minutes=added_time)
        # Field: deliver => yyyy-mm-dd hh:mm:ss
        deliver_time = deliver_time.strftime('%Y-%m-%d %H:%M:%S')

        last_order = Order.select().order_by(Order.code.desc()).first()
        last_order = int(last_order.code) + 1 if last_order else 1

        cost = sum(menu_item.price for menu_item in menu_items)

        desk_query = Desk.select().where(Desk.status == 'free').first()
        if not desk_query:
            return jsonify({'success': False, 'err': 'هیچ میزی خالی نیست'})
        desk_id = desk_query.id

        order = Order(deliver_time, last_order, cost, current_user.id, desk_id, 4, None)
        order.save()
        for menu_item in menu_items:
            item = Items(order.id, menu_item.id)
            item.save()
        return jsonify({'success': True})

    return redirect(url_for('order_history'))

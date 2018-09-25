from flask import Blueprint, render_template, request, url_for
from flask_login import login_required
from config import Config
from app.mod_items import ItemModel

items_page = Blueprint('items_page', __name__, template_folder='templates')


@items_page.route('/itemspage')
@login_required
def items_show():
    page = request.args.get('page', 1, type=int)

    items = ItemModel.query.order_by(ItemModel.id.asc()).paginate(page, Config.ITEMS_PER_PAGE, False)

    next_url = url_for('items_page.items_show', page=items.next_num) \
        if items.has_next else None
    prev_url = url_for('items_page.items_show', page=items.prev_num) \
        if items.has_prev else None
    return render_template('items/items.html', title='Items page', items=items.items,
                          next_url=next_url, prev_url=prev_url)
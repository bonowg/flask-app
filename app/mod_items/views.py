from flask import Blueprint, render_template
from flask_login import login_required

from app.mod_items import ItemModel

items_page = Blueprint('items_page', __name__, template_folder='templates')


@items_page.route('/itemspage')
@login_required
def items_show():
    items = [item for item in ItemModel.query.all()]
    return render_template('items/items.html', title='Items page', items=items)
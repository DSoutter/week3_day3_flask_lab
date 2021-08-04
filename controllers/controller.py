from app import app
from flask import render_template
from models.order_list import orders

# @app.route('/')
# def index():
#     return "placeholder"

@app.route('/orders')
def index_orders():
    return render_template('index.html', title="CodeClan", orders=orders)

@app.route('/orders/<index>')
def individual_index(index):
    return render_template('order.html', title="Customer's Order", order=orders[int(index)])

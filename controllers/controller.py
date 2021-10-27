from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders = orders)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', order = orders[int(index)-1])
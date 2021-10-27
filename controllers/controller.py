from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders = orders)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', order = orders[int(index)-1])

@app.route('/orders/1')
def order_1():
    return render_template('order.html', order = orders[0])

@app.route('/orders/2')
def order_2():
    return render_template('order.html', order = orders[1])

@app.route('/orders/3')
def order_3():
    return render_template('order.html', order = orders[2])
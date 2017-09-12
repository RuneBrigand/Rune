import os
import sqlite3
from flask import Flask, request, Response
from p import picture,wy,order,addct,check_prds,create_orders
from model import Model

app=Flask(__name__)
app.register_blueprint(picture,url_prefix='/ppp')
app.register_blueprint(wy,url_prefix='/cpp')
app.register_blueprint(order,url_prefix='/od')
app.register_blueprint(addct,url_prefix='/adc')
app.register_blueprint(check_prds,url_prefix='/cpd')
app.register_blueprint(create_orders,url_prefix='/cod')

if __name__ == '__main__':
    app.run('0.0.0.0',6625,debug=True)
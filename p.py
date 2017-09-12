from flask import Blueprint, request, Response
import json
import os
import requests
from model import Model
from modelod import Modelad
from modelmain import Modelm
from modelct import Modelc

picture=Blueprint('ppp', __name__)
wy=Blueprint('cpp',__name__)
order=Blueprint('od',__name__)
addct=Blueprint('adc',__name__)
check_prds=Blueprint('cpd',__name__)
create_orders=Blueprint('cod',__name__)

def write_json(data, code=200, info=''):
    result={
        'code':code,
        'data':data,
        'info':info
    }
    return json.dumps(result)

@picture.route('/show_pic/')
def show_pic():
    #f=open('/home/rune/code/cp/static/0.jpg','rb')
    #a=f.read()
    #f.close()
    a=requests.get('http://img1.dongqiudi.com/fastdfs1/M00/A2/9E/o4YBAFl64uSAVfwfAAJGvoThzGg341.jpg')
    #a='hello'
    return Response(a,mimetype='image/jpeg')
    #return Response(a, mimetype='text/plain')

@wy.route('/show_page/')
def show_page():
    b='hello'
    return Response(b,mimetype='text/plain')

@order.route('/orders/',methods=['POST'])
def show_order_detail():
    model=Model()
    customers_id=request.args.get('cus_id')
    data=model.check_order(customers_id)
    return Response(write_json(data),mimetype='application/json')


@addct.route('/adcts/',methods=['POST'])
def add_to_carts():
    model=Modelad()
    customers_id = request.args.get('cus_id')
    quant=request.args.get('quantity')
    products_id=request.args.get('prds_id')
    a=model.add_carts(customers_id,quant,products_id)
    return Response(write_json(a), mimetype='application/json')


@check_prds.route('/products/',methods=['GET'])
def checkp():
    model=Modelm()

    data=model.mainmenu()
    return Response(write_json(data),mimetype='application/json')


@create_orders.route('/crtod/',methods=['POST'])
def add_to_carts():
    model=Modelc()
    customers_id = request.args.get('cus_id')
    products_id = request.args.get('prds_id')
    a=model.add_orders(customers_id,products_id)
    return Response(write_json(a), mimetype='application/json')

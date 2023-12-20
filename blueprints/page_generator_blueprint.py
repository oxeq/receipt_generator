from flask import Blueprint
from flask import Flask, render_template
from objects.db import db
from sqlalchemy import select, delete
import random
import string
from flask import request
import json

page_generator_blueprint = Blueprint('currencies', __name__)


@page_generator_blueprint.route('/receipt/generate', methods=['poas'])
def genereator():

    try:
        admin_key = request.json['admin_key']
        payment_number = request.json['payment_number']
        target = request.json['target']
        date = request.json['date']
        steam_login = request.json['steam_login']
        deposit_sum = request.json['deposit_sum']
        payment_sum = request.json['payment_sum']
        uuid = request.json['uuid']
    except:
        return json.dumps({'success': False, 'error': 0})

    # тут данные заносятся в бд

    return json.dumps({'success': True})



@page_generator_blueprint.route('/receipt/<uuid>', methods=['get'])
def render(uuid):

    # тут иницилизируюются данные из бд по uuid


    return render_template(
        'page.html',
        payment_number=payment_number,
        target=target,
        date=date,
        steam_login=steam_login,
        deposit_sum=deposit_sum,
        payment_sum=payment_sum
        )
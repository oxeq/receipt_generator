import json
import pytz

from datetime import datetime
from flask import Blueprint
from flask import render_template
from objects.db import db
from sqlalchemy import select
from flask import request
from objects.receipt import ReceiptInfo
from auth.auth import check_receipt_token

page_generator_blueprint = Blueprint('page_generator', __name__)


@page_generator_blueprint.route('/add_receipt', methods=['POST'])
@check_receipt_token
def add_receipt():

    try:
        transaction_id = str(request.json['transaction_id'])
        date = int(request.json['date'])
        steam_login = str(request.json['steam_login'])
        sum_ = int(request.json['sum_'])
    except:
        return json.dumps({'success': False, 'error': 0})

    with db.session() as db_session:
        data = db_session.execute(select(ReceiptInfo).where(
            ReceiptInfo.transaction_id == transaction_id,
        ).limit(1)).all()
        db_session.close()

    # проверка информации есть ли такой чек в базе данных
    if len(data) > 0:
        return json.dumps({'success': True})
    else:
        # занесение данных в базу данных
        data = ReceiptInfo(
            transaction_id=transaction_id,
            date=date,
            steam_login=steam_login,
            sum=sum_
        )

        with db.session() as db_session:
            db_session.add(data)
            db_session.commit()
            db_session.close()

        return json.dumps({'success': True})


@page_generator_blueprint.route('/get_receipt', methods=['GET'])
def get_receipt():

    # получение информации о чеке
    try:
        transaction_id = str(request.args['transaction_id'])
    except:
        return json.dumps({'success': False, 'error': 0})

    # получение информации
    with db.session() as db_session:
        data = db_session.execute(select(ReceiptInfo.date, ReceiptInfo.steam_login, ReceiptInfo.sum).where(
            ReceiptInfo.transaction_id == transaction_id,
        ).limit(1)).all()
        db_session.close()

    if len(data) == 0:
        return json.dumps({'success': False, 'error': 1})
    else:

        utc_time = datetime.utcfromtimestamp(data[0][0])
        moscow_tz = pytz.timezone('Europe/Moscow')
        date = utc_time.replace(tzinfo=pytz.utc).astimezone(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        steam_login = data[0][1]
        deposit_sum = data[0][2] / 100

        return render_template(
                'page.html',
                payment_number=transaction_id,
                target='Steam СНГ',
                date=date,
                steam_login=steam_login,
                deposit_sum=deposit_sum,
                payment_sum=deposit_sum
            )
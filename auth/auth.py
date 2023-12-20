from flask import request
from functools import wraps
import requests
import json
from objects.db import db

GENERATE_RECEIPT_TOKEN = 'p9y7fAak9Cemogl'

# проверка запросов администрации
def check_receipt_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            payment_key = request.args['receipt_token']
        except:
            return json.dumps({'success': False, 'error': 'NEED AUTH'})

        if payment_key != GENERATE_RECEIPT_TOKEN:
            return json.dumps({'success': False, 'error': 'NEED AUTH'})
        else:
            return f(*args, **kwargs)

    return decorated

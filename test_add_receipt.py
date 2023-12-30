import requests
from datetime import datetime
import pytz


def convert_to_timestamp(json_data):

    uzbekistan_timezone = pytz.timezone('Asia/Tashkent')
    date_object = datetime.strptime(json_data['date'], '%d.%m.%Y %H:%M:%S')
    date_object = uzbekistan_timezone.localize(date_object)
    timestamp = int(date_object.timestamp())

    json_data['date'] = timestamp

    return json_data



if __name__ == '__main__':

    json_data = {
        'transaction_id': '73616c86-9a73-453e-b78d-0b9a3fc393a7',
        'date': '12.12.2023 19:30:31',
        'steam_login': 'sasha22833111',
        'sum_': 170
    }

    json_data = convert_to_timestamp(json_data)

    response = requests.post('https://receiptforgames.ru/add_receipt?receipt_token=p9y7fAak9Cemogl', json=json_data)
    print(response.json())
import requests

if __name__ == '__main__':

    json_data = {
        'transaction_id': 'XQGYDVRA.',
        'date': 1703072253,
        'steam_login': 'heavenly00001',
        'sum_': 4858
    }
    response = requests.post('http://127.0.0.1:8881/add_receipt?receipt_token=p9y7fAak9Cemogl', json=json_data)
    print(response.json())
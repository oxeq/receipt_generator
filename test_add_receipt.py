import requests

if __name__ == '__main__':

    json_data = {
        'transaction_id': '1qsdqweqwe',
        'date': 1,
        'steam_login': 'faceitrelaxxx',
        'sum_': 10
    }
    response = requests.post('http://127.0.0.1:8881/receipt/add_receipt?receipt_token=p9y7fAak9Cemogl', json=json_data)
    print(response.json())
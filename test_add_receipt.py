import requests

if __name__ == '__main__':

    json_data = {
        'transaction_id': '263942f0-9f21-11e2-9ec1-1800200c9a66',
        'date': 1703072253,
        'steam_login': 'faceitrelaxxxfaceitrelaxxxfaceitrelaxxxfaceitrelaxxx',
        'sum_': 533
    }
    response = requests.post('http://127.0.0.1:8881/receipt/add_receipt?receipt_token=p9y7fAak9Cemogl', json=json_data)
    print(response.json())
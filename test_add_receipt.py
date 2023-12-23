import requests

if __name__ == '__main__':

    json_data = {
        'transaction_id': '2eab2f74-a105-11ee-8c90-0242ac120001',
        'date': 1703072253,
        'steam_login': 'heavenly00001',
        'sum_': 4858
    }
    response = requests.post('https://receiptforgames.ru/add_receipt?receipt_token=p9y7fAak9Cemogl', json=json_data)
    print(response.json())
import requests

# content = requests.get('https://www.floatrates.com/daily/idr.json')
# json_data = content.json()

json_data = {
    'eur': {
        'code': 'EUR',
        'alphaCode': 'EUR',
        'numericCode': '978',
        'name': 'Euro',
        'rate': 5.8201710021279e-05,
        'date': 'Tue, 3 Sep 2024 23:55:12 GMT',
        'inverseRate': 17181.625756948},
    'usd': {
        'code': 'USD',
        'alphaCode': 'USD',
        'numericCode': '840',
        'name': 'U.S. Dollar',
        'rate': 6.4290300280942e-05,
        'date': 'Tue, 3 Sep 2024 23:55:12 GMT',
        'inverseRate': 15554.445937103}
}

for data in json_data.values():
    print(data['code'], data['name'], data['date'], data['inverseRate'])

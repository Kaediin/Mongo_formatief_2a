from pymongo import MongoClient
from pprint import pprint

client = MongoClient(port=27017)
db = client.ontwikkelomgeving


# products = db.products.find({})

def eis1():
    products = db.products.find({}, {'name': 1, 'price': 1})
    eersteProduct = products[0]
    pprint(f'Name: {eersteProduct["name"]}')
    pprint(f'Price: €{eersteProduct["price"]["selling_price"]}')


def eis2(char):
    # products = db.products.find({'name': { '$regex': '(\s+R|^R)', '$options': 'i' }}, {'name': 1}) #this works? It gives a different result
    products = db.products.find({}, {'name': 1})
    for product in products:
        if product['name'][0] == char:
            pprint(product['name'])
            return


def eis3():
    products = db.products.find({}, {'price': 1})
    data = {'sum_total': 0, 'count': 0}
    for product in products:
        try:
            price = product['price']['selling_price']
            data['sum_total'] += float(price)
            data['count'] += 1
        except KeyError:
            pass
    pprint(data)
    pprint(f'Average price: {data["sum_total"] / data["count"]}')


eis1()
eis2('R')
eis3()

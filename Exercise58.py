from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name' : 'My Store',
        'items': [
            {
                'name' : 'My item',
                'price' : 15.99
            }
        ]
    },
    {
        "items": [
            {
                "name": "12kg de amora",
                "price": 12.45
            }
        ],
        "name": "LojinhasLucas"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': request_data['items']
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/new_store')
def create_store2():
    new_store = {
        'name' : 'LojinhasAndre',
        'items': [
            {
                'name' : '10kg de farinha',
                'price' : 1.99
            }
        ]
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})



@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'store not found'})
    
app.run(port=5000)
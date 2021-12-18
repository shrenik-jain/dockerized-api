import requests
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/test"
mongo = PyMongo(app)
db = mongo.db

# Test API    
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'hello_world'


@app.route('/city_alert', methods =['POST'])
def city_alert():
    my_col = db.col
    content = request.get_json()
    city = content['city']
    alert = content['alert']

    query = {"city" : city, "alert_1" : alert}
    doc = my_col.find(query)
    s = doc.count()
    total = my_col.find({"alert_1" : alert}).count()

    return str(city) + " and " + str(alert) + " = " + str(s/total * 100) + " %"


@app.route('/alert_each', methods =['POST'])
def alert_each():
    my_col = db.col

    content = request.get_json()
    city = content['city']
    dic = {}

    for i in my_col.distinct("alert_1"):
        query = {"city" : city, "alert_1" : i}
        doc = my_col.find(query)
        count = doc.count()
        total = my_col.find({"city" : city}).count()

        dic[i] = str(count/total * 100) + "%"

    return jsonify(dic)


@app.route('/delete_range', methods =['POST'])
def delete_range():
    my_col = db.col

    content = request.get_json()
    start_date = content['start_date']
    end_date = content['end_date']

    x = my_col.remove({"$and":[{"date": { "$gte": start_date, "$lt": end_date }}]})

    return x


@app.route('/choose', methods = ['POST'])
def choose():
    content = request.get_json()
    option = content['option']

    if option == 'city_alert':
        r = requests.post("http://0.0.0.0:5000/city_alert", json = content)

    elif option == 'alert_each':
        r = requests.post("http://0.0.0.0:5000/alert_each", json = content)

    else:
        r = requests.post("http://0.0.0.0:5000/delete_range", json = content)

    return r.text


if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = 5000)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
my_col = mydb["my_col"]

city = input()
alert = input()

for i in my_col.distinct("alert_1"):
    query = {"city" : city, "alert_1" : i}

    doc = my_col.find(query)
    count = doc.count()
    total = my_col.find({"city" : city}).count()

    print(total)
    print(count)
    print(i, count/total * 100, "%")
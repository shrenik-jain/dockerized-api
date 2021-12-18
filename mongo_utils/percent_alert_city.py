import pymongo

def create_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test"]         #Database name
    my_col = mydb["my_col"]          #Collection name

    city = input()
    alert = input()

    query = {"city" : city, "alert_1" : alert}

    doc = my_col.find(query)
    s = doc.count()
    total = my_col.find({"alert_1" : alert}).count()

    print("No. of Alerts", s)
    print("Total", total)
    print(s/total * 100, "%")
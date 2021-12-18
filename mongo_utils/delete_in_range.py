import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
my_col = mydb["my_col"]

date_start, time_start = input().split() 
date_end, time_end = input().split()

# date_start = "05/13/21 16:07:54"
# date_end = "05/13/21 16:08:03"

print(my_col.count())
x = my_col.remove({"$and":[{"date": { "$gte": date_start, "$lt": date_end }}]})
print(x)
print(my_col.count())
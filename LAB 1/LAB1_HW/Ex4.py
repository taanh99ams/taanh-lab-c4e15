from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db["customers"]
customers = customers.find()

count_events = 0
count_ads = 0
count_wom = 0

for customer in customers:
    if customer["ref"] == "events":
        count_events += 1
    elif customer["ref"] == "ads":
        count_ads += 1
    else:
        count_wom += 1
print("The number of customer acquired from events, ads and word of mouths is {0}, {1}, {2} respectively".format(count_events, count_ads, count_wom))

from matplotlib import pyplot
labels = ["Events","Advertisement","Word of mouth"]
values = [count_events, count_ads, count_wom]
colors = ["red", "yellow", "green"]

pyplot.pie(values, labels=labels, colors=colors)
pyplot.axis("equal")

pyplot.show()

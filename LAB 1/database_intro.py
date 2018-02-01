from pymongo import MongoClient

mongo_uri = "mongodb://admin_c4e15:techkidc4e15@ds119258.mlab.com:19258/c4e15"

# Open connection to db
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

games = db["games"]

# #3. Create new doc
# new_game = {
#     "title": "GTA",
#     "description": "Steal the road"
# }

# #4. Put the created doc into collection
# games.insert_one(new_game)

games = games.find()
for game in games:
    print(game)

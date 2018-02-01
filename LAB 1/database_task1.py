from pymongo import MongoClient

mongo_uri = "mongodb://admin_c4e15:techkidc4e15@ds119258.mlab.com:19258/c4e15"

client = MongoClient(mongo_uri)
db = client.get_default_database()

blogs = db["Blogs"]

new_blog = {
    "Blog 1": "Energy",
    "Blog 2": "Music",
    "Blog 3": "Vietnam"
}

blogs.insert_one(new_blog)

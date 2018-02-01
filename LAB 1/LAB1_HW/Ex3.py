from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db["posts"]

new_post = {
    "title": "Bai hat cua em",
    "author": "TA",
    "content": '''Ngày đông mưa rét căm
Trên cao mây ngang đầu
Một hai ba bước chân lạc lõng
Dòng xe ơi vút đi, đi theo con phố dài
Lung lay những cành lá
Giấc mơ trơ trụi quá

Em cứ ngân nga một bài hát của người ta
Bài hát của em là tình ca buồn thương lắm
Bài hát của em là lời yêu vùi trong sương
Bên những thơ ngây ngày xưa xa vắng
Em cứ ngân nga từng lời hát của người ta
Lời hát em viết ra là những đớn đau ngút ngàn
Xé nát con tim ai vụn vỡ '''
}

posts.insert_one(new_post)

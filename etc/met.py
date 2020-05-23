from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

db.movies.update_many({'star':target_star},{'$set':{'star':0}})

print(target_movie)
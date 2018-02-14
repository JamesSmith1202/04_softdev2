from pymongo import MongoClient

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

def get_borough(borough):
    return collection.find({'borough': borough})

def get_zipcode(zipcode):
    zipcode = str(zipcode)
    return collection.find({'address.zipcode': zipcode})

def get_zip_grade(zipcode, grade):
    zipcode = str(zipcode)
    grade = str(grade).upper
    return collection.find({'address.zipcode': zipcode, 'grades.grade': grade})

def get_zip_score(zipcode, score):
    zipcode = str(zipcode)
    score = str(score)
    return collection.find({'address.zipcode': zipcode, 'grades.score': {$lt: score}})

print get_borough("Brooklyn")
print get_zipcode("11368")
print get_zip_grade("11368", "A")
print get_zip_score("11368", "10")

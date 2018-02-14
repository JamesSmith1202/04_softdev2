from pymongo import MongoClient

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

def get_borough(borough):
    return collection.find({'borough': borough})

def get_zipcode(zipcode):
    return collection.find({'address.zipcode': zipcode})

def get_zip_grade(zipcode, grade):
    return collection.find({'address.zipcode': zipcode, 'grades.grade': grade})

def get_zip_score(zipcode, score):
    return collection.find({'address.zipcode': zipcode, 'grades.score': {$lt: score}})

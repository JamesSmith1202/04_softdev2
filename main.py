from pymongo import MongoClient
import pprint

connection = MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

def get_borough(borough):
    return collection.find({'borough': borough})

def get_zipcode(zipcode):
    zipcode = str(zipcode)
    return collection.find({'address.zipcode': zipcode})

def get_zip_grade(zipcode, grade):
    zipcode = str(zipcode)
    grade = str(grade).upper()
    return collection.find({'address.zipcode': zipcode, 'grades.grade': grade})

def get_zip_score(zipcode, score):
    zipcode = str(zipcode)
    score = str(score)
    return collection.find({'address.zipcode': zipcode, 'grades.score': { '$lt': score }})

def get_cuisine_borough(cuisine, borough):
    return collection.find({'cuisine': cuisine, 'borough': borough})

def print_restaurants(restaurants):
    for i in restaurants:
        pprint.pprint(i)

print "get_borough(Brooklyn)..."
print_restaurants(get_borough("Brooklyn"))
print("-----------------------------\n")

print "get_zipcode(11368)"
print_restaurants(get_zipcode("11368"))
print("-----------------------------\n")

print "get_zip_grade(11368, A)"
print_restaurants(get_zip_grade("11368", "A"))
print("-----------------------------\n")

print "get_zip_score(11368, 10)"
print_restaurants(get_zip_score("11368", "10"))
print("-----------------------------\n")

print "get_cuisine_borough(Spanish, Queens)"
print_restaurants(get_cuisine_borough("Spanish", "Queens"))
print("-----------------------------\n")
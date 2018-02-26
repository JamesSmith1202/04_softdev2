from pymongo import MongoClient
import pprint

connection = MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

# get restaurants in a particular borough
def get_borough(borough):
    return collection.find({'borough': borough})

# get restaurants in a particular zipcode
def get_zipcode(zipcode):
    zipcode = str(zipcode)
    return collection.find({'address.zipcode': zipcode})

# get restaurants in a particular zipcode with a particular grade
def get_zip_grade(zipcode, grade):
    zipcode = str(zipcode)
    grade = str(grade).upper()
    return collection.find({'address.zipcode': zipcode, 'grades.grade': grade})

# get restaurants in a particular zipcode with scores less than denoted
def get_zip_score(zipcode, score):
    zipcode = str(zipcode)
    return collection.find({'address.zipcode': zipcode, 'grades.score': { '$lt': score }})

# get restaurants in a particular borough with a specific cuisine
def get_cuisine_borough(cuisine, borough):
    return collection.find({'cuisine': cuisine, 'borough': borough})

# print the restaurant name only
def print_restaurants(restaurants):
    for i in restaurants:
        print i['name']

#TESTING
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
print_restaurants(get_zip_score("11368", 10))
print("-----------------------------\n")

print "get_cuisine_borough(Spanish, Queens)"
print_restaurants(get_cuisine_borough("Spanish", "Queens"))
print("-----------------------------\n")

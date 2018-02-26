'''
Wikipedia Movie Data - A database created from scraping american movies from wikipedia
link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json

Import Mechanism:
First the mongo server is checked to confirm that the db isn't there, then the locally downloaded json is opened for read permissions
and passed to json.load to transform it into a python dict. The DB is a big list, so it is iterated through and each entry is added to the db.
A counter is included just so that the user can see their progress during upload because it is a large database(~18800 movies)
'''

from pymongo import MongoClient
from json import load


connection = MongoClient('homer.stuy.edu')
collection = connection.stan_smith_xus #the database
db = collection.movies

#if the database hasnt been made, then make it and add it
if not 'stan_smith_xus' in connection.database_names():
    counter = 0
    f = open("movies.json", "r")
    movies = load(f)
    for movie in movies:
        if(counter % 100 == 0):
            print "Adding database...adding movie #{}".format(counter)
        db.insert_one(movie)
        counter += 1
    f.close()
'''
else: #for debugging, the db is removed if you run the program after making a db on the server
    print "removing..."
    connection.drop_database('stan_smith_xus')
'''

def print_movies(movies):
    for i in movies:
        print i['title'] + " (" + str(i['year']) + ")"

def print_all():
    print_movies(db.find())

def get_by_title(name):
    return db.find({"title": name})

def get_by_genre(genre):
    return db.find({"genre": genre})

def get_by_director(director):
    return db.find({"director": director})

def get_by_year(year):
    return db.find({"year": year})

def get_genre_year(genre, year):
    return db.find({'genre': genre, 'year': year})

def get_after_year(year):
    return db.find({ 'year': { '$gt': year }})

print "\nget_by_title('Finding Dory')...\n"
print_movies(get_by_title("Finding Dory"))

print "\nget_by_genre('Action-adventure')...\n"
print_movies(get_by_genre("Action-adventure"))

print "\nget_by_director('Rich Moore')...\n"
print_movies(get_by_director("Rich Moore"))

print "\nget_by_year(1956)...\n"
print_movies(get_by_year(1956))

print "\nget_after_year(2011)"
print_movies(get_after_year(2011))

print "\nget_genre_year('Action-adventure', 2013)...\n"
print_movies(get_genre_year("Action-adventure", 2013))

connection.close()

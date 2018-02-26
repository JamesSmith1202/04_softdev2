#------------PROBLEMS------------#
#The program is only reading in one entry from the json
#------------PROBLEMS------------#


#http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en

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


connection.close()
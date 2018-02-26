#------------PROBLEMS------------#
#The program is only reading in one entry from the json
#------------PROBLEMS------------#


#http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en

from pymongo import MongoClient
from json import load


connection = MongoClient('homer.stuy.edu')
#if the database hasnt been made, then make it and add it
if not 'stan_smith_xus' in connection.database_names():
    print "i tried"
    collection = connection.stan_smith_xus #the database
    db = collection.events
    with open('events.json') as f:
        event = load(f)
        print event
        db.insert(event)
else: #for debugging, the db is removed if you run the program after making a db on the server
    print "removing..."
    connection.drop_database('stan_smith_xus')

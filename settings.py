import os

# we want to seamlessy run our API both locally and on Heroku. 
# If running on Heroku, sensible DB connection settings are
# stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'user')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'evedemo')





# quick check current settings
if __name__ == "__main__":
    print ("Current settings are")
    print ("MONGO_HOST: %s" % MONGO_HOST)

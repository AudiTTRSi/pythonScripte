def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://anotherUser:g8hAfblzsG5jZYkn@cluster0.bhcbo.mongodb.net/test"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    dbname = get_database()
    # Create the database for our example (we will use the same database throughout the tutorial
    #return client['user_shopping_list']

# This is added so that many files can reuse the function get_database()
#if __name__ == "__main__":

    # Get the database
#    dbname = get_database()

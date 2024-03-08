import pymongo

def get_database(connection_string : str  ):
    CONNECTION_STRING : str  = connection_string
    client  =  pymongo.MongoClient(CONNECTION_STRING)
    return  client['smartphones_db']['smartphones']

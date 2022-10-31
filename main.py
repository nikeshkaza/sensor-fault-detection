from turtle import pd
from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print("CLIENT name:",mongodb_client.database_name)
    print("collection name:",mongodb_client.database.list_collection_names())
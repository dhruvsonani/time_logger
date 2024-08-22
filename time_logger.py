# time_logger.py

import os
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class TimeLogger:
    def __init__(self, mongo_uri="mongodb+srv://dhruvsonani:dhruvsonani1@cluster0.qhxovmz.mongodb.net/time_logging?retryWrites=true&w=majority&appName=Cluster0", db_name="time_logging", collection_name="test1"):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = MongoClient(self.mongo_uri,server_api=ServerApi('1'))
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def log_start_time(self):
        user_id = os.getlogin()
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "user_id": user_id,
            "start_time": start_time,
            "event": "start"
        }
        result = self.collection.insert_one(log_entry)
        print(f"Start time for user {user_id} logged at {start_time} with entry ID {result.inserted_id}")

    def log_end_time(self):
        user_id = os.getlogin()
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "user_id": user_id,
            "end_time": end_time,
            "event": "end"
        }
        result = self.collection.insert_one(log_entry)
        print(f"End time for user {user_id} logged at {end_time} with entry ID {result.inserted_id}")

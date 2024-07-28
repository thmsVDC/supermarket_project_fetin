from database.database import Database
from pymongo.collection import ReturnDocument

db = Database(database="fetin", collection="counter")


def get_next_sequence():
    try:
        ret = db.collection.find_one_and_update(
            {"_id": "supermarket counter"},
            {"$inc": {"seq": 1}},
            return_document=ReturnDocument.AFTER
        )
        if ret is None:
            raise ValueError("Counter document not found.")
        return ret['seq']
    except Exception as e:
        print(f"An error occurred while getting the next sequence: {e}")
        return None


def generate_id_manager():
    try:
        ret = db.collection.find_one_and_update(
            {"_id": "manager counter"},
            {"$inc": {"seq": 1}},
            return_document=ReturnDocument.AFTER
        )
        if ret is None:
            raise ValueError("Counter document not found.")
        return ret['seq']
    except Exception as e:
        print(f"An error occurred while getting the next sequence: {e}")
        return None

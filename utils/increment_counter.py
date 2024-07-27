from database.database import Database
from pymongo.collection import ReturnDocument

db = Database(database="fetin", collection="counter")
COUNTER_ID = "counter"


def get_next_sequence():
    try:
        ret = db.collection.find_one_and_update(
            {"_id": COUNTER_ID},
            {"$inc": {"seq": 1}},
            return_document=ReturnDocument.AFTER
        )
        if ret is None:
            raise ValueError("Counter document not found.")
        return ret['seq']
    except Exception as e:
        print(f"An error occurred while getting the next sequence: {e}")
        return None

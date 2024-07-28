from utils.increment_counter import generate_id_manager


class CrudManager:
    def __init__(self, database):
        self.db = database

    def create_manager(self, name: str, password: str):
        try:
            manager_id = generate_id_manager()
            res = self.db.collection.insert_one({
                "_id": manager_id,
                "name": name,
                "password": password
            })
            print(f"Manager added to the database with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while adding the manager: {e}")
            return None

    def read_manager(self, search):
        try:
            if isinstance(search, int):
                result = self.db.collection.find({"_id": int(search)})
                return list(result)

            result = self.db.collection.find({"_id": {"$gt": 1000}})
            return list(result)

        except Exception as e:
            print(f"An error occurred while reading managers: {e}")
            return []

    def update_manager(self, manager_id: int, updates: dict):
        try:
            result = self.db.collection.update_one(
                {"_id": manager_id},
                {"$set": updates}
            )
            if result.modified_count == 1:
                print(f"Manager with id {manager_id} updated successfully.")
                return True
            else:
                print(f"No manager found with id {manager_id}.")
                return False
        except Exception as e:
            print(f"An error occurred while updating the manager: {e}")
            return False

    def delete_manager(self, manager_id: int):
        try:
            result = self.db.collection.delete_one({"_id": manager_id})
            if result.deleted_count:
                print(f"Manager with id {manager_id} deleted successfully.")
                return True
            else:
                print(f"No manager found with id {manager_id}.")
                return False
        except Exception as e:
            print(f"An error occurred while deleting the manager: {e}")
            return False

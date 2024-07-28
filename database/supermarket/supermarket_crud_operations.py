from utils.increment_counter import get_next_sequence


class CrudProducts:
    def __init__(self, database):
        self.db = database

    def create_product(self, name: str, unit_amount: str, brand: str, quantity: int, price: float, product_type: str,
                       localization: str):
        try:
            product_id = get_next_sequence()
            res = self.db.collection.insert_one({
                "_id": product_id,
                "name": name,
                "unit_amount": unit_amount,
                "brand": brand,
                "quantity": quantity,
                "price": price,
                "product_type": product_type,
                "localization": localization
            })
            print(f"Product added to the database with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while adding the product: {e}")
            return None

    def read_product(self, search: str, operation_type: str):
        try:
            if operation_type == "read":
                result = self.db.collection.find({
                    '$or': [
                        {'name': {'$regex': search, '$options': 'i'}},
                        {'product_type': {'$regex': search, '$options': 'i'}},
                        {'brand': {'$regex': search, '$options': 'i'}}
                    ]
                })
            else:
                result = self.db.collection.find({'_id': int(search)})

            return list(result)
        except Exception as e:
            print(f"An error occurred while reading products: {e}")
            return []

    def update_product(self, product_id: int, updates: dict) -> bool:
        try:
            result = self.db.collection.update_one(
                {"_id": product_id},
                {"$set": updates}
            )
            if result.modified_count == 1:
                print(f"Product with id {product_id} updated successfully.")
                return True
            else:
                print(f"No product found with id {product_id}.")
                return False
        except Exception as e:
            print(f"An error occurred while updating the product: {e}")
            return False

    def delete_product(self, product_id: int) -> bool:
        try:
            result = self.db.collection.delete_one({"_id": product_id})
            if result.deleted_count:
                print(f"Product with id {product_id} deleted successfully.")
                return True
            else:
                print(f"No product found with id {product_id}.")
                return False
        except Exception as e:
            print(f"An error occurred while deleting the product: {e}")
            return False

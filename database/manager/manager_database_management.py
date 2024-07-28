from database.database import Database
from ..manager.manager_crud_operations import CrudManager

db = Database(database="fetin", collection="managers")
crud_manager = CrudManager(db)


def create_manager():
    name = input("Name: ")
    password = input("Password: ")
    crud_manager.create_manager(name, password)


def read_manager():
    search = input("Type de manager ID you want to search: ")
    try:
        search = int(search)
    except ValueError:
        pass
    results = crud_manager.read_manager(search)

    for result in results:
        print(result)


def update_manager():
    try:
        search = int(input('Type de manager ID you want to search: '))
        manager = crud_manager.read_manager(search)

        manager_id = search
        name = str(input(f'Name ({manager[0]["name"]}): ') or manager[0]["name"])
        password = str(input(f'Password ({manager[0]["password"]}): ') or manager[0]["password"])

        updated_manager = {
            "name": name,
            "password": password
        }

        crud_manager.update_manager(manager_id, updated_manager)
    except Exception as e:
        print(f"An error occurred while reading managers: {e}")


def delete_manager():
    manager_id = int(input('Enter the ID of the manager you want to delete: '))
    crud_manager.delete_manager(manager_id)

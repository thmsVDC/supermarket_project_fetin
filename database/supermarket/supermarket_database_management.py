from database.database import Database
from database.supermarket.supermarket_crud_operations import CrudProducts

db = Database(database="fetin", collection="supermarket")
crud_products = CrudProducts(db)


def create_product():
    try:
        name = str(input('Name: '))
        unit_amount = str(input('Unit amount: '))
        brand = str(input('Brand: '))
        quantity = int(input('Quantity: '))
        price = float(input('Price: '))
        product_type = str(input('Type: '))
        localization = str(input('Localization: '))

        crud_products.create_product(name, unit_amount, brand, quantity, price, product_type, localization)
        print("Product created successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def read_product():
    search = input("Search: ")
    regex_pattern = f'.*{search}.*'
    results = crud_products.read_product(regex_pattern, "read")

    for result in results:
        print(result)

    return results


def update_product():
    search = input('Type the product id you want to update: ')
    product = crud_products.read_product(search, "update")
    try:

        # Get updated values from the user
        product_id = int(search)
        name = str(input(f'Name ({product[0]["name"]}): ') or product[0]["name"])
        unit_amount = str(input(f'Unit amount ({product[0]["unit_amount"]}): ') or product[0]["unit_amount"])
        brand = str(input(f'Brand ({product[0]["brand"]}): ') or product[0]["brand"])
        quantity = int(input(f'Quantity ({product[0]["quantity"]}): ') or product[0]["quantity"])
        price = float(input(f'Price ({product[0]["price"]}): ') or product[0]["price"])
        product_type = str(input(f'Type ({product[0]["product_type"]}): ') or product[0]["product_type"])
        localization = str(input(f'Localization ({product[0]["localization"]}): ') or product[0]["localization"])

        updated_product = {
            "name": name,
            "unit_amount": unit_amount,
            "brand": brand,
            "quantity": quantity,
            "price": price,
            "product_type": product_type,
            "localization": localization
        }

        crud_products.update_product(product_id, updated_product)
    except ValueError as e:
        print(f"Invalid input: {e}")


def delete_product():
    product_id = int(input('Enter the ID of the product you want to delete: '))
    crud_products.delete_product(product_id)


class Document:
    def __init__(self, product_id, name, unit_amount, brand, quantity, price, type, localization):
        self.product_id = product_id
        self.name = name
        self.unit_amount = unit_amount
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.type = type
        self.localization = localization

    def __repr__(self):
        return (
            f"Document(product_id={self.product_id!r}, "
            f"name={self.name!r}, "
            f"unit_amount={self.unit_amount!r}, "
            f"brand={self.brand!r}, "
            f"quantity={self.quantity!r}, "
            f"price={self.price!r}, "
            f"type={self.type!r}, "
            f"localization={self.localization!r})"
        )


def dict_to_doc(dictionary):
    return Document(**dictionary)

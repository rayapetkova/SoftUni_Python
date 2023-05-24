from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for some_product in self.products:
            if some_product.name == product_name:
                return some_product

    def remove(self, product_name):
        for some_product in self.products:
            if some_product.name == product_name:
                self.products.remove(some_product)

    def __repr__(self):
        final = []

        for some_product in self.products:
            final.append(f"{some_product.name}: {some_product.quantity}")

        return str('\n'.join(final))

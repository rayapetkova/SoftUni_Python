from django.db import models


class ProductManager(models.Manager):

    def available_products(self):
        all_available_products = self.filter(is_available=True)
        return all_available_products

    def available_products_in_category(self, category_name: str):
        all_available_by_category = self.filter(
            category__name=category_name,
            is_available=True)

        return all_available_by_category

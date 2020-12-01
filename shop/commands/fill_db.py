import os
import json

from django.core.management.base import BaseCommand
from shop.models import Category, Product

JSON_PATH = 'shop/json'


# def load_from_json(file_name):
#     with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
#         return json.load(infile)


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


encoding = 'utf-8'


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

# Create your views here.
from shop.models import Category, Product


def get_category(request):
	categories = Category.objects.filter(is_active=True)
	return categories


def get_products(request):
	products = Product.objects.filter(is_active=True)
	return products

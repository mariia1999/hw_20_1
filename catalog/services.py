from django.core.cache import cache

from catalog.models import Product
from config.settings import CASHE_ENABLED


def get_product_from_cache():
    """ получает данные из кэша"""
    if not CASHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product


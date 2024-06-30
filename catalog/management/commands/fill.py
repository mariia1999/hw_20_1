import psycopg2
from django.core.management import BaseCommand

import json

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # подключение к базе данных
        with psycopg2.connect(database='Catalog', user='postgres', password='alisa2812') as conn:
            with conn.cursor() as cur:

                # удаление данных из таблицы Category и Product
                cur.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY')
                conn.commit()
                cur.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE')
                conn.commit()

                # соединение с файлом, в котором находятся все данные о категориях и продуктах
                with open('catalog_data.json', 'r', encoding='utf-8') as f:
                    js_f = json.load(f)

                    # создание категории
                    category_for_create = []
                    product_for_create = []
                    for c in js_f:
                        if c['model'] == 'catalog.category':
                            category_for_create.append(Category(**c['fields']))
                    Category.objects.bulk_create(category_for_create)

                    # Создание продукта
                    id_p = 1
                    for c in js_f:
                        if c['model'] == 'catalog.product':
                            product_for_create.append(
                                Product(id=id_p, category_id=c['fields']['category'], name=c['fields']['name']))
                            id_p += 1
                        Product.objects.bulk_create(product_for_create)
                        conn.autocommit = True
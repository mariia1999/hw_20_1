# Generated by Django 4.2.2 on 2024-09-10 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "price"],
                "permissions": [
                    ("can_cancel_publication", "Can cancel publication"),
                    ("can_change_description", "Can change description"),
                    ("can_change_category", "Can change category"),
                ],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
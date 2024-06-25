# Generated by Django 5.0.6 on 2024-06-24 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "product_description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование товара",
                        max_length=100,
                        verbose_name="Наименование товара",
                    ),
                ),
                (
                    "product_description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание товара",
                        null=True,
                        verbose_name="Описание товара",
                    ),
                ),
                (
                    "product_photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото товара",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Фото товара",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Введите стоимость товара",
                        verbose_name="Цена за покупка",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        help_text="Введите дату создания товара",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        help_text="Введите дату последнего изменения",
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию товара",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория товара",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["category", "price"],
            },
        ),
    ]
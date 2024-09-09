from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    product_description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )
    product_description = models.TextField(
        verbose_name="Описание товара",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    product_photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото товара",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        help_text="Введите категорию товара",
        null=True,
        blank=True,
        related_name="catalog",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите стоимость товара"
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату создания товара",
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )
    owner = models.ForeignKey(
        User, verbose_name='Владелец', help_text='Укажите владельца товара',
        blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category", "price"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Версия",
    )
    v_num = models.CharField(
        max_length=100,
        verbose_name="№ версии",
        help_text="Введите № версии",
    )
    v_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    curr_v = models.BooleanField(
        verbose_name="Признак текущей версии",
        help_text="Активно?"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product"]

    def __str__(self):
        return f"Наименование продукта - {self.product}, Версия - {self.v_num}"
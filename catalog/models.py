from django.db import models


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
        related_name='catalog',
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите стоимость товара"
    )
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Введите дату создания товара",
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category", "price"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
    )
    content = models.CharField(
        max_length=1000,
        verbose_name="Содержимое",
        help_text="Введите текст",
    )
    preview = models.ImageField(
        upload_to="BlogPost/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото"
    )
    created_at = models.DateField(
        verbose_name="Дата создания", auto_now_add=True,
    )
    is_published = models.BooleanField(default=False),
    view_count = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите кол-во просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Блог-пост"
        verbose_name_plural = "Блог-посты"

    def __str__(self):
        return self.title



# Generated by Django 5.0.6 on 2024-07-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.CharField(
                blank=True,
                help_text="Введите ссылку",
                max_length=50,
                unique=True,
                verbose_name="Ссылка",
            ),
        ),
    ]

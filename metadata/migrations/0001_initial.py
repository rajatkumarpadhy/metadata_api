# Generated by Django 4.2.1 on 2023-05-10 14:31

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
                ("category_id", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                ("location_id", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SKU",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("subcategory", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("subcategory_id", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategories",
                        to="metadata.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Department",
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
                ("department_id", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departments",
                        to="metadata.location",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="metadata.department",
            ),
        ),
    ]

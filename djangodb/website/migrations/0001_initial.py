# Generated by Django 4.1.6 on 2023-02-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("fname", models.CharField(max_length=50, null=True)),
                ("lname", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=100, null=True)),
                ("passwd", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Orgazniation",
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
                ("orgName", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]

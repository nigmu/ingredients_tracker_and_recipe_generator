# Generated by Django 4.1 on 2024-06-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image_upload", "0004_alter_upload_image_class_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="upload_image_class",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]

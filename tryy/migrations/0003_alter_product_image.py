# Generated by Django 4.1.5 on 2023-01-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryy', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]

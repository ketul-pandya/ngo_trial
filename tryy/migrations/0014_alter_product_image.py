# Generated by Django 4.1.5 on 2023-02-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryy', '0013_delete_ketul_signup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='tryy/static'),
        ),
    ]

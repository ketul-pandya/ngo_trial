# Generated by Django 4.1.5 on 2023-01-28 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tryy', '0007_signup_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password',
            new_name='passsword',
        ),
    ]

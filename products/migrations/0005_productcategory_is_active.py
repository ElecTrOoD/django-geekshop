# Generated by Django 3.2.3 on 2021-08-31 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_alter_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 3.2.3 on 2021-08-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
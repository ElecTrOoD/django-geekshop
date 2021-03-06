# Generated by Django 3.2.3 on 2021-08-05 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=150, verbose_name='тэги')),
                ('about_me', models.TextField(blank=True, verbose_name='о себе')),
                ('gender',
                 models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=1, verbose_name='пол')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

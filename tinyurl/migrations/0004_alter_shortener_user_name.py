# Generated by Django 4.2.2 on 2023-06-19 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tinyurl', '0003_alter_shortener_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='user_name',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

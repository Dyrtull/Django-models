# Generated by Django 3.2.2 on 2023-10-23 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comic',
            options={},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'comic', 'verbose_name_plural': 'comics'},
        ),
        migrations.AddField(
            model_name='wishlist',
            name='marvel_id',
            field=models.PositiveIntegerField(default=1, unique=True, verbose_name='marvel id'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='stock_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='stock qty'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wished_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='wished_qty'),
        ),
        migrations.AlterModelTable(
            name='comic',
            table=None,
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table='e_commerce_comics',
        ),
    ]
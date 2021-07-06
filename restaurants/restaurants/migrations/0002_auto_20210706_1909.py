# Generated by Django 3.1.8 on 2021-07-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name': 'Пицца', 'verbose_name_plural': 'Пиццы'},
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.CharField(blank=True, max_length=128, verbose_name='Сыр'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pastry',
            field=models.CharField(blank=True, max_length=128, verbose_name='Тесто'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='secret_ingredient',
            field=models.CharField(blank=True, max_length=128, verbose_name='Секретный ингридиент'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=128, verbose_name='Адрес'),
        ),
    ]
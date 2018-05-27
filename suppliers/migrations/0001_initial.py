# Generated by Django 2.0.3 on 2018-03-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sup_name', models.CharField(max_length=50, verbose_name='Название поставщика')),
                ('sup_address', models.CharField(max_length=50, verbose_name='Адрес поставщика')),
                ('sup_cont', models.TextField(verbose_name='Контактные данные')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]

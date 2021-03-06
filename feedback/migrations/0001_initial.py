# Generated by Django 2.0.3 on 2018-03-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, help_text='Пожалуйста, введите ваше имя...', max_length=50, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, default=None, help_text='Пожалуйста, введите фамилиую...', max_length=50, null=True, verbose_name='Фамилия')),
                ('sex', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский'), ('none', 'Не указывать')], default='none', help_text='Пожалуйста, укажите ваш пол...', max_length=10, verbose_name='Пол')),
                ('tel', models.CharField(blank=True, default='+38-', help_text='Пожалуйста, введите ваш телефон...', max_length=25, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(help_text='Пожалуйста, введите ваш Email...', max_length=254, verbose_name='Email')),
                ('question', models.TextField(help_text='Пожалуйста, задайте вопрос...', verbose_name='Вопрос')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('replied', models.BooleanField(default=False, verbose_name='Отвечено')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]

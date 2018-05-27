from django.db import models
from django.forms import ModelForm
#from future import unicode_literals
from django.utils import timezone
# Create your models here.


sexs = (
    ('male', 'Мужской'),
    ('female', 'Женский'),
    ('none', 'Не указывать'),
    )

class subscriber(models.Model):
    username = models.CharField(max_length = 50, blank=True, default=None, null=True, verbose_name="Имя")
    # last_name = models.CharField(max_length = 50, blank=True, default=None, null=True, verbose_name="Фамилия", help_text="Пожалуйста, введите фамилиую...")
    sex = models.CharField(max_length = 10, choices = sexs, default="none", verbose_name="Пол")
    tel = models.CharField(max_length = 25, blank=True, null=True, default = "+38-", verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    question = models.TextField(verbose_name="Вопрос", help_text="Пожалуйста, задайте вопрос...")
    reply = models.TextField(verbose_name="Отет администратора", blank=True, default=None, null=True,)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Обновлён")
    replied = models.BooleanField(default=False, verbose_name="Отвечено")

    def __str__(self):
        try:
            return "%s" %(self.last_name)
        except:
            return '%s' % self.id
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

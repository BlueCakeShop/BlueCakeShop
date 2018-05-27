from django.db import models
from django.forms import ModelForm
#from future import unicode_literals
from django.utils import timezone
# Create your models here.

class info(models.Model):
    user_name = models.CharField(max_length = 50, verbose_name="Имя", help_text="Пожалуйста, введите ваше имя...")
    question_theme = models.CharField(max_length = 50, verbose_name="Тема вопроса", help_text="Пожалуйста, введите тему вопроса...")
    question = models.TextField(verbose_name="Ваш вопрос", help_text="Задайте Ваш вопрос...")
    reply = models.TextField(blank=True, null=True, verbose_name="Ответ администратора")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Обновлён")
    replied = models.BooleanField(default=False, verbose_name="Отвечено")
    def __str__(self):
        try:
            return "%s - %s" %(self.user_name, self.replied)
        except:
            return '%s' % self.id
    class Meta:
        verbose_name = 'Вопрос поситителей'
        verbose_name_plural = 'Вопросы поситителей'

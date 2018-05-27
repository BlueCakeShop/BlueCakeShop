from django.db import models
from django.forms import ModelForm
#from future import unicode_literals
from django.utils import timezone
# Create your models here.

class supplier(models.Model):
	sup_name = models.CharField(max_length = 50, verbose_name="Название поставщика")
	sup_address = models.CharField(max_length = 50, verbose_name="Адрес поставщика")
	sup_cont = models.TextField(verbose_name="Контактные данные")
	
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Обновлён")
	
	def __str__(self):
		try:
			return "%s" %(self.sup_name)
		except:
			return '%s' % self.id
			
	class Meta:
		verbose_name = 'Поставщик'
		verbose_name_plural = 'Поставщики'

from django.db import models
from django.core.validators import URLValidator
from django.urls import reverse



# Create your models here.
# class Category(models.Model):
#     category_name = models.CharField(max_length = 64, db_index=True, blank=True, default=None, verbose_name="Категория")
#     category_slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     category_description = models.TextField(blank=True, default=None, verbose_name="Опиание котегории")
#     category_is_active = models.BooleanField(default=True, verbose_name="Активная")
#     def __str__(self):
#         try:
#             return "%s" %(self.category_name)
#         except:
#             return '%s' % self.id
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#     def get_absolute_url(self):
#         return reverse('products:product_list_by_category', args=[self.category_slug])
#
# class Category_photo(models.Model):
#     category = models.ForeignKey(Category, blank=True, default=None, null=True, verbose_name="Категория", on_delete=models.CASCADE)
#     category_photo = models.ImageField(upload_to='products/product_category_photos/', verbose_name="Фотограифя")
#     category_photo_is_active = models.BooleanField(default=True, verbose_name="Активная")
#     category_photo_is_main = models.BooleanField(default=False, verbose_name="Главная (превью)")
#     category_photo_created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создана")
#     category_photo_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменена")
#
#     def __str__(self):
#         try:
#             return "%s" %(self.image.url)
#         except:
#             return '%s' % self.id
#     class Meta:
#         verbose_name = 'Фотография категории'
#         verbose_name_plural = 'Фотографии категорий'


class Product(models.Model):
    # product_category = models.ForeignKey(Category, blank=True, default=None, verbose_name="Категория товара", on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 200, db_index=True, blank=True, default=None, verbose_name="Наименование")
    product_slug = models.SlugField(max_length=200, db_index=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    product_description = models.TextField(blank=True, default=None, verbose_name="Описание")
    product_stock = models.PositiveIntegerField(verbose_name="На складе")
    product_is_active = models.BooleanField(default=True, verbose_name="Активный")

    product_created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    product_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменён")

    def __str__(self):
        try:
            return "%s - %s" %(self.product_name, self.product_price)
        except:
            return '%s' % self.id
    class Meta:
        ordering = ['product_name']
        index_together = [
            ['id', 'product_slug']
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
          return reverse('products:product_detail', args=[self.id, self.product_slug])

class Product_photo(models.Model):
    product = models.ForeignKey(Product, blank=True, default=None, null=True, verbose_name="Товар", on_delete=models.CASCADE)
    product_photo = models.ImageField(upload_to='products/products_images/', verbose_name="Фотограифя")
    product_photo_is_active = models.BooleanField(default=True, verbose_name="Активная")
    product_photo_is_main = models.BooleanField(default=False, verbose_name="Главная (превью)")
    product_photo_created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создана")
    product_photo_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменена")

    def __str__(self):
        try:
            return "%s" %(self.image.url)
        except:
            return '%s' % self.id
    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'

class Product_comments(models.Model):

    # Валидация на максимальный размер фото
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Максимальный размер файла: %sMB" % str(megabyte_limit))

    pc_product = models.ForeignKey(Product, blank=True, default=None, verbose_name="Товар", on_delete=models.CASCADE)
    pc_user_name = models.CharField(max_length = 50, verbose_name="Имя", help_text="Пожалуйста, введите ваше имя...")
    pc_comment = models.TextField(verbose_name="Ваш вопрос", help_text="Задайте Ваш вопрос...")
    # pc_video = models.CharField(validators=[URLValidator()], max_length=200, blank=True, default=None, verbose_name="Вложить видео", help_text="Ссылка на видео...")
    # pc_photo = models.ImageField(upload_to='products/comments_images/', blank=True,verbose_name="Фотография")
    # pc_photo = models.ImageField(upload_to='products/comments_images/', blank=True,verbose_name="Фотография", validators=[validate_image])
    pc_reply = models.TextField(blank=True, null=True, verbose_name="Ответ администратора")
    pc_replied = models.BooleanField(default=False, verbose_name="Отвечено")
    pc_created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    pc_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменён")

    def __str__(self):
        try:
            return "Комментарий к %s " %(self.pc_product)
        except:
            return '%s' % self.id
    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комментарии'

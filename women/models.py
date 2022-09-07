from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


''' class ProductType(models.Model):
        name = models.CharField(max_length=100, db_index=True, verbose_name='Тип товара')

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Тип товара'
            verbose_name = 'Типы товаров'


    class Order(models.Model):
        name = models.CharField(max_length=100, db_index=True, verbose_name='Название товара')
        ptype = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Тип товара')
        date = models.DateTimeField(verbose_name='Дата доставки')
        photo = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Файл')

        class Meta:
            verbose_name = 'Заказ'
            verbose_name = 'Заказы'

'''
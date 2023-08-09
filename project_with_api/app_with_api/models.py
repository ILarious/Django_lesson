from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    publish_date = models.DateField(verbose_name='Дата публикации')
    comments = models.ManyToManyField('Comment')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    user_name = models.CharField(max_length=25, verbose_name='Имя')
    text = models.TextField(
        null=True,
        blank=True,
        verbose_name='Текст'
    )
    publish_date = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
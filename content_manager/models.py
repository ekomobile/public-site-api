from django.db import models


class City(models.Model):
    date_in = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    date_change = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Изменено')
    name = models.CharField(max_length=30, verbose_name='Название города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Segment(models.Model):
    date_in = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    date_change = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Изменено')
    name = models.CharField(max_length=30, verbose_name='Название сегмента')
    description = models.TextField(max_length=250, verbose_name='Описание сегмента')

    class Meta:
        verbose_name = 'Сегмент рынка'
        verbose_name_plural = 'Сегменты рынка'

    def __str__(self):
        return self.name


class MobileOperator(models.Model):
    date_in = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    date_change = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Изменено')
    name = models.CharField(max_length=30, verbose_name='Название оператора')
    bg_color = models.CharField(max_length=8, verbose_name='цвет фона HEX')
    font_color = models.CharField(max_length=8, verbose_name='цвет шрифта HEX')

    class Meta:
        verbose_name = 'Мобильный оператор'
        verbose_name_plural = 'Мобильные операторы'

    def __str__(self):
        return self.name

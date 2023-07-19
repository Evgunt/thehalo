from django.db import models


class Catalog(models.Model):
    title = models.CharField(unique=False, max_length=300, blank=False, default="", verbose_name='Заголовок')
    content = models.CharField(unique=False, max_length=300, blank=False, default="", verbose_name='Габариты',
                               help_text='Через зяпятую')
    img = models.ImageField(default="", blank=False, verbose_name='Картинка', upload_to='img')

    class Meta:
        verbose_name_plural = 'Каталог'
        verbose_name = 'Каталог'

    def __str__(self):
        return self.title


class Size(models.Model):
    length = models.CharField(unique=False, default="", max_length=300, blank=False, verbose_name='Длина')
    width = models.CharField(unique=False, default="", max_length=300, blank=False, verbose_name='Ширина')
    heit = models.CharField(unique=False, default="", max_length=300, blank=False, verbose_name='Высота')

    class Meta:
        verbose_name_plural = 'Размерные ряд'
        verbose_name = 'Размерный ряд'

    def __str__(self):
        return self.length


class Slider(models.Model):
    title = models.CharField(unique=False, default="", max_length=300, blank=False, verbose_name='Название')
    img = models.ImageField(default="", blank=False, verbose_name='Картинка', upload_to='img')

    class Meta:
        verbose_name_plural = 'Наше производство'
        verbose_name = 'Наше производство'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(unique=False, default="", max_length=300, blank=False, verbose_name='Название')
    img = models.ImageField(default="", blank=False, verbose_name='Картинка', upload_to='img')

    class Meta:
        verbose_name_plural = 'О нас (картинки)'
        verbose_name = 'О нас (картинки)'

    def __str__(self):
        return self.title


class Sertificate(models.Model):
    title = models.CharField(unique=False, default="", max_length=300, blank=False, verbose_name='Название')
    img = models.ImageField(default="", blank=False, verbose_name='Картинка', upload_to='img')

    class Meta:
        verbose_name_plural = 'Сертификаты'
        verbose_name = 'Сертификат'

    def __str__(self):
        return self.title

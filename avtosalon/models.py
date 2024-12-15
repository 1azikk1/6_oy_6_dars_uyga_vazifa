from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)
    brand_country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'brend '
        verbose_name_plural = 'brendlar'


class Car(models.Model):
    name = models.CharField(max_length=50, verbose_name='avtomobil nomi')
    color = models.CharField(max_length=20, verbose_name='rangi')
    photo = models.ImageField(upload_to='post/photos', verbose_name='rasmi')
    year = models.IntegerField(verbose_name='ishlab chiqarilgan yili')
    price = models.IntegerField(verbose_name='narxi')
    views = models.IntegerField(default=0, verbose_name='korishlar soni')
    horsepower = models.IntegerField(verbose_name='ot kuchi')
    added = models.DateTimeField(auto_now=True, verbose_name='qoshilgan vaqti')
    is_available = models.BooleanField(default=True, verbose_name='mavjud yoki yoq', help_text='Galochka turgan bolsa mavjud, aks holda esa mavjud emas!')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='brendi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'avtomobil '
        verbose_name_plural = 'avtomobillar'
        ordering = ('-pk',)

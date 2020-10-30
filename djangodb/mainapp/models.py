from django.db import models

class CategorySight(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория достопримечательности'
        verbose_name_plural = 'Категории достопримечательностей'


class Sight(models.Model):
    category = models.ForeignKey(CategorySight,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    states = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


class RenovatedSight(models.Model):
    category = models.ForeignKey(Sight,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рестоврация'
        verbose_name_plural = 'Рестоврации'


class Reviews(models.Model):
    category = models.ForeignKey(Sight,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
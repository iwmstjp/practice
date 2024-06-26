from django.db import models
from django.utils import timezone


class BaseMeta(models.Model):
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

    class Meta:
        abstract = True


class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    memo = models.TextField()
    web_site = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'person'
        index_together = [['first_name', 'last_name']]
        ordering = ['salary']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=20)
    school = models.ForeignKey(
        'Schools', on_delete=models.PROTECT
    )

    class Meta:
        db_table='students'

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.age}'

class Schools(models.Model):
    name = models.CharField(max_length=20)
    prefecture = models.ForeignKey(
        'Prefectures', on_delete=models.PROTECT
    )

    class Meta:
        db_table = 'schools'


class Prefectures(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'prefectures'


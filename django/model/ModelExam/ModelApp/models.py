from django.db import models


# Create your models here.
class Tests(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table='tests'


class TestResults(models.Model):
    student_id = models.ForeignKey(
        'Students', on_delete=models.CASCADE
    )
    test_id = models.ForeignKey(
        'Tests', on_delete=models.CASCADE
    )
    score = models.IntegerField()
    class Meta:
        db_table='testreults'


class Students(models.Model):
    class_id = models.ForeignKey(
        'Classes', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    class Meta:
        db_table='students'


class Classes(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table='classes'

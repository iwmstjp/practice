import os
from random import randint
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes

def make_date():
    class_names = ['Class' + c for c in 'ABCDEFGHIJ']
    student_names = ['Student' + c for c in 'ABCDEFGHIJ']
    test_names = ['math', 'english', 'language']

    inserted_tests = []
    for test_name in test_names:
        test = Tests(
            name=test_name
        )
        test.save()
        inserted_tests.append(test)

    for class_name in class_names:
        insert_class = Classes(
            name=class_name
        )
        insert_class.save()
        for student_name in student_names:
            name = class_name + ' ' + student_name
            student = Students(
                name=name,
                class_fk=insert_class,
                grade=1
            )
            student.save()
            for inserted_test in inserted_tests:
                test_result=TestResults(
                    student=student,
                    test=inserted_test,
                    score=randint(50,100)
                )
                test_result.save()

from django.db.models import Sum, Avg, Max, Min
for summary in Classes.objects.values('name', 'students__testresults__test__name').annotate(
    max_score=Max('students__testresults__score'),
    min_score=Min('students__testresults__score'),
    avg_score=Avg('students__testresults__score'),
    sum_score=Sum('students__testresults__score')
):
    print(summary['name'],
          summary['students__testresults__test__name'],
          summary['max_score'],
          summary['min_score'],
          summary['avg_score'],
          summary['sum_score']
          )

for summary in Students.objects.values('class_fk__name', 'testresults__test__name' ).annotate(
        max_score=Max('testresults__score'),
        min_score=Min('testresults__score'),
        avg_score=Avg('testresults__score'),
        sum_score=Sum('testresults__score')
):
    print(summary['class_fk__name'],
          summary['testresults__test__name'],
          summary['max_score'],
          summary['min_score'],
          summary['avg_score'],
          summary['sum_score']
          )
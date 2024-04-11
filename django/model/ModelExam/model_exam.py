import os
from random import randint
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes

# class_names = ['Class' + c for c in 'ABCDEFGHIJ']
# student_names = ['Student' + c for c in 'ABCDEFGHIJ']
# test_names = ['math', 'english', 'language']
#
# inserted_tests = []
# for test_name in test_names:
#     test = Tests(
#         name=test_name
#     )
#     test.save()
#     inserted_tests.append(test)
#
# for class_name in class_names:
#     insert_class = Classes(
#         name=class_name
#     )
#     insert_class.save()
#     for student_name in student_names:
#         name = class_name + ' ' + student_name
#         student = Students(
#             name=name,
#             class_id=insert_class,
#             grade=1
#         )
#         student.save()
#         for inserted_test in inserted_tests:
#             test_result = TestResults(
#                 student_id=student,
#                 test_id=inserted_test,
#                 score=randint(50,100)
#             )
#             test_result.save()

from django.db.models import Sum, Avg, Max, Min

# for cs in Classes.objects.values('name', 'students__testresults__test_id').annotate(
#   max_score=Max('students__testresults__score')
# ):
#     print(cs['name'], cs['max_score'])

# for cs in Classes.objects.values('name', 'students__testresults__tests__name').annotate(
#   max_score=Max('students__testresults__score')
# ):

# print(Classes.objects.values('name','students__testresults__test_id'))
print(Students.objects.values('name', 'testresults__tests__name'))
# print(Classes.objects.values('name', 'students__testresults__tests__name'))
# print(Classes.objects.values('name', 'students__testresults__score'))


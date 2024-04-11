import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

prefectures =['Tokyo', 'Osaka']
schools = ['east', 'west', 'north', 'south']
students = ['taro', 'jiro', 'naruto']


def insert_records():
    for prefecture_name in prefectures:
        prefecture = Prefectures(
            name=prefecture_name
        )
        prefecture.save()
        for school_name in schools:
            school = Schools(
                name=school_name,
                prefecture=prefecture
            )
            school.save()
            for student_name in students:
                studnent = Students(
                    name=student_name,
                    age=17,
                    major='CS',
                    school=school
                )
                studnent.save()

def select_students():
    students = Students.objects.all()
    for s in students:
        print(s.id, s.name, s.school.id, s.school.name, s.school.prefecture.id, s.school.prefecture.name)

# Students.objects.filter(school=1).delete()
# Schools.objects.filter(id=1).delete()
# print(Students.objects.all())
# Prefectures.objects.filter(id=1).delete()
# insert_records()
# select_students()
# s = Schools.objects.first()
# # st = Students.objects.first()
# print(dir(s.students_set))
# st = s.students_set
# print(type(st))
# print(dir(st))
# print(st.all())
# print(s.prefecture.name)
# print(dir(st))
# print(st.school.prefecture.name)
# print(dir(st.school.prefecture))

# print(Students.objects.all()[:6])
# print(Students.objects.filter(name="taro", pk__gte=40).all())

# print(Students.objects.filter(name__startswith="t").all())

from django.db.models import Q
# print(Students.objects.filter(Q(name="taro") | Q(pk__gt=19)).all())
# print(Students.objects.values('name','school').all())
# print(Students.objects.exclude(name='taro'))
# print(Students.objects.filter(id__in=[5,9]))
# print(Students.objects.filter(id__contains='1'))
# st = Students.objects.order_by('name','-id')
# for s in st:
#     print(s)
# print(Students.objects.order_by('name'))
st = Students.objects.filter(school__name='east').exclude(prefecture__name='Tokyo')
for s in st:
    print(s, s.school.name, s.school.prefecture.name)
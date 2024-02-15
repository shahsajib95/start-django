import random

from faker import Faker

from .models import *

fake = Faker()

from django.db.models import Sum


def create_subject_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
               subject_obj = SubjectMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(10, 100)
               )
                
    except Exception as e:
        print(e)


def seed_db(n=10):
    try:
        for _ in range(0, n):
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)
            department = department_objs[random_index]
            
            student_id = f'STU-0{random.randint(100, 999)}'
            student_id_obj = StudentID.objects.create(student_id=student_id)
            
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()
            
            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
    except Exception as e:
        print(e)


def generate_report_card():
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', 'student_age')
    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i)
        i = i + 1
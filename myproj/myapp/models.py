from email.policy import default
from pyexpat import model
from django.db import models
from random import randint

studentID = randint(1000000,9999999)
parentID = randint(1000000,9999999)
instructorID = randint(1000000,9999999)
courseID = randint(1000,9999)

class Parent(models.Model):
    #---and student need modifications---
    parent_id = models.IntegerField(default=parentID, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.IntegerField()
    #parent should recieve parent ID from parent Table
    #parent can have many children
    

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    

# Create your models here.
class Student(models.Model):
    #--- and Parent need modifications---
    student_id = models.IntegerField(default=studentID, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #parent should recieve parent ID from parent Table
    #child can have many parents
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduated'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='FR'
    )

    def __str__(self):
        return "%s %s %s" % (self.student_id, self.first_name, self.last_name)

    class Meta:
        ordering = ['student_id', 'first_name', 'last_name']
    

class Instructor(models.Model):
    #--- and course need modifications---
    instructor_id = models.IntegerField(default=instructorID, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_num = models.IntegerField()
    #instructor can have many courses


    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.email, self.phone_num)

class Course(models.Model):
    #---Instructor needs modifications---
    course_id = models.IntegerField(default=courseID)
    course_name = models.CharField(max_length=100)
    # time = models.TimeField()
    #Course can have many instructor
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['course_name']

class Schedule(models.Model):
    #--everything needs modification---
    #One student to one schedule
    student_id =models.ForeignKey(Student, on_delete=models.CASCADE)
    #each from a course
    course_1 = models.ForeignKey(Course, on_delete=models.CASCADE)
    

    def __str__(self):
        return "%s" % (self.course_1)

    class Meta:
        ordering = ['course_1']

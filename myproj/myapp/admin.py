from django.contrib import admin
from .models import *

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
        list_display=['instructor_id', 'first_name', 'last_name', 'email','phone_num', 'course']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ['course_id', 'course_name', 'instructor']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'student_id', 'parent', 'year_in_school']    

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display= ['parent_id', 'first_name', 'last_name', 'email', 'phone_num']

# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ['student_id', 'course1', 'course2', 'course3', 'course4', 'course5', 'course6']


# admin.py
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age', 'enrollment_date', 'course')
    # search_fields = ('first_name', 'last_name', 'email', 'course')
    # list_filter = ('course', 'enrollment_date')

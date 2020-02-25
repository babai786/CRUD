from django.contrib import admin
from pratikapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['sname','sno','smarks']
    search_fields = ['sname']

admin.site.register(Student,StudentAdmin)

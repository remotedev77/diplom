from django.contrib import admin
from app.models import *
# Register your models here.


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')
    search_fields = ('name',)

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty_id', 'duration')
    list_filter = ('faculty_id', 'duration')
    search_fields = ('name', 'faculty_id__name')
    raw_id_fields = ('faculty_id',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'specaialty_id', 'date_created')
    list_filter = ('specaialty_id',)
    search_fields = ('name', 'specaialty_id__name')
    raw_id_fields = ('specaialty_id',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'user_id', 'group_id')
    search_fields = ('name', 'surname', 'user_id__username')
    raw_id_fields = ('user_id', 'group_id')

@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'salary', 'position', 'user_id')
    list_filter = ('position',)
    search_fields = ('name', 'surname', 'user_id__username')
    raw_id_fields = ('user_id',)

# syllabus/admin.py
from django.contrib import admin
from .models import Faculty, SyllabusFile

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(SyllabusFile)
class SyllabusFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty', 'uploaded_at')
    list_filter = ('faculty',)
    search_fields = ('title', 'faculty__name')
    ordering = ('faculty__name', 'title')
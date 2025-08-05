from django.contrib import admin
from .models import Subject, Topic, Note

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('subject',)
    search_fields = ('name',)
    ordering = ('subject__name', 'name')
    list_select_related = ('subject',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'uploaded_at', 'has_pdf', 'short_content')
    list_filter = ('topic__subject',)
    search_fields = ('title', 'content')
    date_hierarchy = 'uploaded_at'
    ordering = ('-uploaded_at',)
    list_select_related = ('topic', 'topic__subject')

    def has_pdf(self, obj):
        return bool(obj.pdf_file)
    has_pdf.boolean = True
    has_pdf.short_description = 'PDF उपलब्ध'

    def short_content(self, obj):
        return obj.content[:75] + '...' if obj.content else ''
    short_content.short_description = 'पूर्वावलोकन'

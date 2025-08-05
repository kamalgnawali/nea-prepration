# quiz/admin.py
from django.contrib import admin
from .models import Category, Question, Option

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class OptionInline(admin.TabularInline): # Question भित्र Option हरू देखाउन
    model = Option
    extra = 4 # डिफल्टमा ४ वटा खाली Option फिल्ड देखाउने
    min_num = 2 # कम्तीमा २ वटा Option हुनुपर्ने

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category')
    list_filter = ('category',)
    search_fields = ('text',)
    inlines = [OptionInline] # Question मा Option हरू सिधै थप्न मिल्ने बनाउने
    # quiz/admin.py
from .models import QuizAttempt

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'score', 'total_questions', 'date_taken')

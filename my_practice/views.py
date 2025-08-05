from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Note,Category, Question
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def notes_view(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})

def quiz_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = Question.objects.filter(category=category)

    return render(request, 'quiz.html', {
        'category': category,
        'questions': questions
    })

def quiz_by_category(request, category_id):
    # logic for showing quiz by category
   return render(request, 'quiz_result.html')
def quiz_category_list(request):
    categories = Category.objects.all()
    return render(request, 'quiz_category_list.html', {'categories': categories})
from django.shortcuts import render

def contact_view(request):
    return render(request, 'contact.html')

# syllabus/views.py
from django.shortcuts import render, get_object_or_404
from .models import Faculty, SyllabusFile

def faculty_list(request):
    """
    सबै संकायहरूको सूची देखाउने।
    """
    faculties = Faculty.objects.all()
    context = {
        'faculties': faculties,
        'page_title': 'सिलेबस - संकायहरू',
    }
    return render(request, 'faculty_list.html', context)

def syllabus_detail(request, faculty_slug):
    """
    एक खास संकायको सिलेबस फाइलहरू देखाउने।
    """
    faculty = get_object_or_404(Faculty, slug=faculty_slug)
    syllabus_files = SyllabusFile.objects.filter(faculty=faculty).order_by('title')
    
    context = {
        'faculty': faculty,
        'syllabus_files': syllabus_files,
        'page_title': f'{faculty.name} सिलेबस',
    }
    return render(request, 'syllabus_detail.html', context)
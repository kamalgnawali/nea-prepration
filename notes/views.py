# notes/views.py
from django.shortcuts import render, get_object_or_404
from .models import Subject, Topic, Note

def subject_list_view(request):
    """
    सबै विषयहरूको सूची देखाउने (जस्तै: Electrical, Computer, Mechanical)।
    """
    subjects = Subject.objects.all().order_by('name')
    context = {
        'subjects': subjects,
        'page_title': 'नोटहरू - विषयहरू',
    }
    return render(request, 'subject_list.html', context)

def topic_detail_view(request, subject_slug, topic_slug=None):
    """
    एक खास विषयका टपिकहरू र यदि कुनै टपिक चयन गरिएको छ भने त्यसको नोट देखाउने।
    """
    subject = get_object_or_404(Subject, slug=subject_slug)
    topics = subject.topics.all().order_by('name') # त्यस विषयका सबै टपिकहरू

    selected_topic = None
    note_content = None # नोटको टेक्स्ट सामग्री
    note_pdf_url = None # नोटको PDF फाइल URL
    print(f"DEBUG: note_pdf_url for {topic_slug}: {note_pdf_url}")
    if topic_slug:
        selected_topic = get_object_or_404(Topic, subject=subject, slug=topic_slug)
        # यहाँ हामीले नोट खोज्छौं
        note = Note.objects.filter(topic=selected_topic).first() # एउटा टपिकको एउटा मात्र नोट मान्दै
        if note:
            note_content = note.content
            if note.pdf_file:
                note_pdf_url = note.pdf_file.url

    context = {
        'subject': subject,
        'topics': topics,
        'selected_topic': selected_topic,
        'note_content': note_content,
        'note_pdf_url': note_pdf_url,
        'page_title': f'{subject.name} नोट्स',
    }
    return render(request, 'topic_detail.html', context)
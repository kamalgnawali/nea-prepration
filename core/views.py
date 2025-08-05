from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm

def about_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save or send mail
            messages.success(request, 'तपाईंको सन्देश सफलतापूर्वक पठाइयो!')
            return redirect('about')
        else:
            messages.error(request, 'कृपया फर्म सही रूपमा भरिएको छ कि छैन जाँच गर्नुहोस्।')
    return render(request, 'about.html', {'form': form})

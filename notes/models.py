# notes/models.py
from django.db import models
from django.utils.text import slugify

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True) # टपिकको छोटो विवरण

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    # यहाँ तपाईंले नोटको सामग्री टेक्स्टको रूपमा वा PDF फाइलको रूपमा राख्न सक्नुहुन्छ
    # यदि टेक्स्ट मात्र हो भने:
    content = models.TextField(blank=True, null=True)
    # यदि PDF फाइल हो भने:
    pdf_file = models.FileField(upload_to='notes_pdfs/', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['topic__name', 'title']
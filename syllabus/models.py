# syllabus/models.py
from django.db import models
from django.utils.text import slugify

class Faculty(models.Model):
    """
    NEA को विभिन्न संकायहरू (जस्तै: Civil, Computer, Electrical)
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="संकायको नाम")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL Slug")
    description = models.TextField(blank=True, verbose_name="संकायको बारेमा")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "संकाय"
        verbose_name_plural = "संकायहरू"
        ordering = ['name'] # नाम अनुसार क्रमबद्ध गर्ने

class SyllabusFile(models.Model):
    """
    प्रत्येक संकायसँग सम्बन्धित PDF फाइल।
    """
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='syllabus_files', verbose_name="संकाय")
    title = models.CharField(max_length=200, verbose_name="फाइलको शीर्षक")
    file = models.FileField(upload_to='syllabus_pdfs/', verbose_name="PDF फाइल") # 'syllabus_pdfs/' भित्र फाइलहरू अपलोड हुन्छन्
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="अपलोड मिति")

    def __str__(self):
        return f"{self.faculty.name} - {self.title}"

    class Meta:
        verbose_name = "सिलेबस फाइल"
        verbose_name_plural = "सिलेबस फाइलहरू"
        ordering = ['faculty__name', 'title']
# quiz/models.py
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug: # यदि slug खाली छ भने, name बाट स्वतः बनाउने
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    # अरू fields थप्न सक्नुहुन्छ

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    # अरू fields थप्न सक्नुहुन्छ (जस्तै: image, difficulty)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.question.text[:50]} - {self.text}" # प्रश्नको सुरुको ५० अक्षर र Option text देखाउने
    # quiz/models.py
from django.db import models
from django.contrib.auth.models import User
from .models import Category  # यदि category model छ भने

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category.name} ({self.score})"

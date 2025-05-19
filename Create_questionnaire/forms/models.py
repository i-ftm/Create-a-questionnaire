from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} (ساخته شده توسط: {self.owner.username})"

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', 'متن'),
        ('radio', 'تک‌گزینهای'),
        ('checkbox', 'چندگزینهای'),
    )
    form = models.ForeignKey(Form,on_delete=models.CASCADE,related_name='questions')
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    is_required = models.BooleanField(default=False)
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_At = models.DateTimeField(auto_now_add=True)
    
class Answer(models.Model):
    response  = models.ForeignKey(Response, on_delete= models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    
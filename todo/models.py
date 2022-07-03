from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    color = ColorField(default='#ffffff')
    
    def __str__(self):
        return self.name

def get_sentinel():
    return Lesson.objects.get_or_create(name="placeholder", teacher="none", color="#FFFFFF")
    
class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=get_sentinel()[0].id, null=False)
    title = models.CharField(max_length=100, blank=False)
    pub_date = models.DateField("Date Published", default=timezone.now)
    due_date = models.DateField("Due Date", blank=False)
    description = models.CharField(max_length=1000, blank=False)
    attachment = models.URLField(max_length=300, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    reminder = models.DateTimeField("Reminder", blank=True, null=True)
    
    def __str__(self):
        return self.title
    

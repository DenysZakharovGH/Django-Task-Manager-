from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
#use for min and max values in stasus_in_percents field

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    doer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    STATUS_CHOICES = (
                    ('new', 'new'),
                    ('inp', 'in process'),
                    ('d', 'done'),
                    ('rj', 'reject')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='new')
    stasus_in_percents = models.IntegerField(validators=[MinValueValidator(0),
                                                         MaxValueValidator(100)],
                                             default=0)

    deadline = models.DateField(default=datetime.now(), blank=True)

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.title

class Cheklist(models.Model):
    task = models.ForeignKey(Task, related_name='cheklists', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    body = models.CharField(max_length=100)
    class Meta:
        ordering = ['-id']



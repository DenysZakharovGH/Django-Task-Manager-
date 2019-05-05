from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    def __str__(self):
        return self.name




class Task(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True )
    STATUS_CHOICES = (
        ('new', 'new'),
        ('inp', 'in process'),
        ('d', 'done'),
        ('rj', 'reject')
    )

    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='new')
    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    questions = [
        ('color', 'What is your favorite color?'),
        ('animal', 'What is your favorite animal?'),
        ('food', 'What is your favorite food?'),
        ('movie', 'What is your favorite movie?'),
        ('book', 'What is your favorite book?'),
        ('song', 'What is your favorite song?'),
        ('tv_show', 'What is your favorite TV show?'),
        ('video_game', 'What is your favorite video game?'),
        ('sport', 'What is your favorite sport?'),
        ('hobby', 'What is your favorite hobby?'),
    ]
    sec_questions = models.CharField(max_length=100, choices=questions, default='color')
    sec_answer = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50)
    phno = models.CharField(max_length=10)

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=300)
    year = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    achievement = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.degree

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Tools', 'Tools'),
    ]
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.CharField(max_length=50)
    certificate = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return self.title

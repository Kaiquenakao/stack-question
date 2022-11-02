from django.db import models
from datetime import datetime

class Project(models.Model):
    TECHNOLOGY = (
        (0, "JavaScript"),
        (1, "Java"),
        (2, "Python"),
        (4, "Android"),
        (5, "Apple"),
        (6, "Other")
    )

    now = datetime.now()
    
    project_id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    github = models.CharField(max_length=500)
    technology = models.IntegerField(choices=TECHNOLOGY, default=6)
    summary = models.TextField(max_length=200)
    #description = HTMLField()
    date_created = models.DateTimeField(default=now)
    project_image = models.ImageField(blank=True)

    class Meta:
        ordering = ['technology']

    def __str__(self):
        return self.title

    def technology_verbose(self):
        return dict(Project.TECHNOLOGY)[self.technology]
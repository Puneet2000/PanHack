from django.db import models

class ResearchPost(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=5000)
    link = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.Title,self.Description,self.link)


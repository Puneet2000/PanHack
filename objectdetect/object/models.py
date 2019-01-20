from django.db import models


class QueryImage(models.Model):
    query_image = models.FileField(upload_to='images/')
    name = models.CharField(max_length=500)
    long = models.CharField(max_length=500, default="")
    lat = models.CharField(max_length = 500, default="")
    aadhar = models.CharField(max_length = 500, default="")
    category = models.CharField(max_length = 500, default="spam")

    class Meta:
        db_table = 'query_images'

class Worker(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length = 100, default = "")


class Assigned(models.Model):
    query = models.ForeignKey(QueryImage, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    logs = models.CharField(max_length=1000, default="Going On!")

from django.db import models


class QueryImage(models.Model):
    query_image = models.FileField(upload_to='images/')
    name = models.CharField(max_length=500)
    long = models.CharField(max_length=500, default="")
    lat = models.CharField(max_length = 500, default="")
    aadhar = models.CharField(max_length = 500, default="")
    category = models.CharField(max_length = 500, default="spam")
    status = models.CharField(max_length = 100, default = "pending")

    class Meta:
        db_table = 'query_images'


class Work(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    class Meta:
        db_table = 'work_people'
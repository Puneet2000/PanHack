from django.db import models


class QueryImage(models.Model):
    query_image = models.FileField(upload_to='images/')
    name = models.CharField(max_length=500)
    long = models.CharField(max_length=500, default="")
    lat = models.CharField(max_length = 500, default="")
    aadhar = models.CharField(max_length = 500, default="")

    class Meta:
        db_table = 'query_images'

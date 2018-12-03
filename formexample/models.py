from django.db import models


class Collage(models.Model):
    collage_name=models.CharField(max_length=100)
    collage_email=models.EmailField()
    collage_address=models.CharField(max_length=250)
    collage_city = models.CharField(max_length=100)

    class Meta:
        db_table = 'collage'
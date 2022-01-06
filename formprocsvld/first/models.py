from django.db import models

# Create your models here.


class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    file=models.FileField(upload_to='static//upload//')
    class Meta:
        db_table = "developer"

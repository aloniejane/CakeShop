from django.db import models

# Create your models here.
class Customers(models.Model):
    name=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()

    def __str__(self):
        return self.name
        return self.name

    class Meta:
        db_table="Customers"

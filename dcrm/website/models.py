from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=25)
    last_name  = models.CharField(max_length=25)
    email = models.EmailField(max_length=40,null=True)
    phone =models.CharField(max_length=11)
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=40)
    state = models.CharField(max_length=10)
    pincode= models.CharField(max_length=6)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

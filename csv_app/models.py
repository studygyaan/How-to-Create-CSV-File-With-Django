from django.db import models

# Create your models here.
class UserDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = "userdetails"
    
    def __str__(self) : 
        return self.first_name
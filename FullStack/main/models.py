from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def get_user_id(self):
        return self.id
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    class Meta:
        db_table = "User information"
        db_table_comment = "This is where the information of the users stored."
from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# from django.db import models
# Create your models here.
class Employee(models.Model):
    empId = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    address = models.TextField(max_length=100)


    def __str__(self):
        return f"empId: {self.empId},name: {self.name},  phone: {self.phone}, email: {self.email} and address: {self.address}"




# class CustomUser(models.Model):
#     email = models.EmailField(unique=True)
#     # password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    
#     # Add related_name to avoid clash with auth.User's user_permissions
#     user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions")
#     empId = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     REQUIRED_FIELDS = ['email'] 
#     def __str__(self):
#         return self.username
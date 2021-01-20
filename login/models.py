from django.db import models

# Create your models here.
class UserTable(models.Model):
    empid=models.CharField(max_length=100,null=False,unique=True)
    emp_name=models.CharField(max_length=100,null=False)
    email_id=models.CharField(max_length=100,null=False,unique=True)
    password=models.CharField(max_length=100,null=False)
    proj_manager=models.CharField(max_length=100,null=False)
    secret_code=models.CharField(max_length=100,null=False)
    role=models.CharField(max_length=10,null=False,choices=(('Admin','Admin'),('User','User')),default='User')

    def __str__(self):
        return self.empid

from django.db import models 
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    password=models.CharField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name']
    
    objects=UserManager()
    
    
    
class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='categories/')#categories folder
    
class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField()
    image=models.ImageField(upload_to='products/')
    description=models.TextField(max_length=300)
    Category=models.ForeignKey('Category',on_delete=models.CASCADE)#CASCADE-deleting category with everything in it
    
    
    
    

    
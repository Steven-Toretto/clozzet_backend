from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)#hashed password shown in dashboard
        return user
    
    #creating super user
    def create_superuser(self, email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be set to True for a superuser')
        if extra_fields.get ('is_superuser') is not True:
            raise ValueError('is_staff must be set to True')
        
        return self.create_user(email, password, **extra_fields)
            
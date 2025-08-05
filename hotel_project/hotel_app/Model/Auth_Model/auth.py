from django.db import models
from django.contrib.auth.hashers import make_password

class Auth_user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField()
    
    def save(self,*args,**kargs):
        if not self.password.startswith('pdfdk_2'):
            self.password=make_password(self.password)
        super().save(*args,**kargs)
    def __str__(self):
        return self.username

    
    
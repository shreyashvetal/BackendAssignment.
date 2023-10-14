from django.db import models
from hashlib import sha512

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    def validate_password(self,shared_password):
        hashstring = f"{self.username}|{shared_password}"
        generated_hash = sha512(hashstring.encode('utf-8')).hexdigest().lower()
        return True if generated_hash == self.password else False
    
    @staticmethod
    def generate_hash(username, shared_password):
         hashstring = f"{username}|{shared_password}"
         generated_hash = sha512(hashstring.encode('utf-8')).hexdigest().lower()
         return generated_hash
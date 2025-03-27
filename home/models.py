from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    user_phone = models.CharField(max_length=15, unique=True)
    user_password = models.CharField(max_length=128)  # Stores hashed password
    remember_me_token = models.CharField(max_length=255, null=True, blank=True)  # For "Remember Me" functionality
    password_reset_token = models.CharField(max_length=255, null=True, blank=True)  # For "Forgot Password" functionality
    password_reset_expiry = models.DateTimeField(null=True, blank=True)  # Expiry for password reset token

    def __str__(self):
        return self.user_email
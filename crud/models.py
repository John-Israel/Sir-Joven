from django.db import models

# Create your models here.

class Genders(models.Model):
    class Meta:
        db_table = 'genders_tbl'
    gender_id = models.BigAutoField(primary_key=True, blank=False)
    gender = models.CharField(max_length=55, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    class Meta:
        db_table = 'users_tbl'
    user_id = models.BigAutoField(primary_key=True, blank=False)
    full_name = models.CharField(max_length=64, blank=False)
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=False)
    address = models.CharField(max_length=254, blank=False)
    contact_number = models.CharField(max_length=16, blank=True)
    email = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=64, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
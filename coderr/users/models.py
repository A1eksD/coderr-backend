from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractUser):
    TYPE_CHOICES = [
        ('customer', 'Kunde'),
        ('business', 'Anbieter'),
    ]
    username = models.CharField(max_length=50, unique=True)
    file = models.FileField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    tel = PhoneNumberField(unique=True, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    working_hours = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    created_at = models.DateField(default=now)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=False)    
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    groups = models.ManyToManyField( #hizufügen der Berechtigung wegen AbstractUser, weil dieser das nciht aufgelistet ist
        'auth.Group', 
        related_name='customuser_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField( #hizufügen der Berechtigung wegen AbstractUser, weil dieser das nciht aufgelistet ist
        'auth.Permission', 
        related_name='customuser_set', 
        blank=True
    )

    def __str__(self):
        return f'{self.username, " " ,self.email, " ", self.id}'




class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
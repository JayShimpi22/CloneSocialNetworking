from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import UserManager
from user.managers import CustomUserManager

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
    ('None','Prefer not to say'),
]

# Create your models here.
class User(AbstractUser):
    img = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    bio = models.TextField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True,choices=GENDER_CHOICES)
    is_private_account = models.BooleanField(null=True,blank=True)

    first_name = None
    last_name = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    @property
    def follower_count(self):
        cnt = self.follow_followed.count()
        return cnt
    
    @property
    def following_count(self):
        cnt = self.follow_follower.count()
        return cnt
    
    @property
    def posts_count(self):
        cnt = self.postmodel_set.all().count()
        return cnt
    

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,username,**kwargs):
        if not email:
            raise ValueError(ugettext_lazy('email invalid'))
        email = self.normalize_email(email)
        user = self.model(email=email,username = username,**kwargs)
        # user = User.model(email=email,**extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,username,**kwargs):
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_staff',True) 
        kwargs.setdefault('is_superuser',True) 

        if kwargs.get('is_active') is not True:
            raise ValueError(ugettext_lazy('is_staff must be True'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('is_superuser must be True'))
        return self.create_user(email,password,username,**kwargs)
        




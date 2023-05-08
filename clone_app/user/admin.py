from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import UserForm,CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        ('Personal Details',{'fields':('email','full_name','username','img','password1','password2')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
        ('Optional',{'fields':('bio','website')})
    )
    fieldsets = (
        ('Personal Details',{'fields':('email','full_name','username','img')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
        ('Optional',{'fields':('bio','website')})

    )

admin.site.register(User,CustomUserAdmin)

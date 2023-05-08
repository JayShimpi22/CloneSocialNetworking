from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('img','full_name','username','email','bio','website','phone_number','gender','is_private_account')

        labels = {
            'is_private_account': 'Do you want to make your account private ?'
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            if field == 'img':
                self.fields[field].widget.attrs.update({'class':'form-control-file'})
            elif field == 'is_private_account':
                self.fields[field].widget.attrs.update({'class':'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class':'form-control form-control-sm'})
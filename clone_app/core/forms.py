from django import forms
from core.models import PostModel
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('text','image',)
        widgets = {
            'text':forms.TextInput(attrs = {
                'class':'form-control form-control-sm',
                'placeholder':'Caption this',
            }
            )
        }    
    
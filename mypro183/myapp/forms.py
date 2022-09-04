from django import forms
from myapp.models import Student

class StuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
                    'name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'phone':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'mail':forms.TextInput(attrs={'class':'form-control form-control-sm',}),
                    'message':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    #'User':forms.Select(attrs={'class':'form-control form-control-sm',}),
                    }

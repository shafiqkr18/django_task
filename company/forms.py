from django import forms
from .models import Company, Department


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('author','title', 'contact','email','industrytype','text')

        # add widgets if you want
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('author','title', 'text',)

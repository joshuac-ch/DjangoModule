from django import forms

class CreateFormsUser(forms.Form):
    username=forms.CharField()
    profile=forms.CharField()
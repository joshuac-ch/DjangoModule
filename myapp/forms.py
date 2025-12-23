from django import forms

class CreateFormsUser(forms.Form):
    username=forms.CharField()
    profile=forms.CharField()

class CreateFormPr(forms.Form):
    user=forms.CharField()
    img=forms.CharField()    
from django import forms
 
class Search(forms.Form):
    tag = forms.CharField(max_length=10)
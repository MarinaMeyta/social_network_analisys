from django import forms
 
class Search(forms.Form):
    text = forms.CharField(max_length=50)
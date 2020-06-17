from django import forms
from .models import Friend


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "mail", "gender", "age", "birthday"]


class FindForm(forms.Form):
    find = forms.CharField(label="Find", required=False)
    

class CheckForm(forms.Form):
    required = forms.IntegerField(label="Required")
    min = forms.IntegerField(label="Min", min_value=100)
    max = forms.IntegerField(label="Max", max_value=1000)
    
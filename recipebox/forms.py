from django import forms

from recipebox.models import *


class AuthorAddForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    bio = forms.CharField(widget=forms.Textarea)


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=160)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    # title = models.CharField("Title of recipe", max_length=50)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # description = models.CharField("Description of the recipe", max_length=50)
    # time_required = models.IntegerField("Time Required to make recipe")
    # instructions = models.TextField("Recipe instructions")

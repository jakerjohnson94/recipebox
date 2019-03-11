from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Author, Recipe
from .forms import *


def recipe_list(request):
    recipes = Recipe.objects.all
    return render(request, "recipe_list.html", {"recipes": recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.filter(author=author_id)
    return render(
        request, "author_detail.html", {"author": author, "recipes": recipes}
    )


def logout_action(request):
    html = "logout.html"
    logout(request)
    return redirect(request.GET.get("next", "/"))


def login_view(request):
    html = "login.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


@staff_member_required(login_url="/login/")
def useradd(request):
    html = "formadd.html"
    form = None

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            username = data["username"]
            raw_password = data["password1"]
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(request.GET.get("recipes/"))

    else:
        form = UserCreationForm()
    return render(request, "useradd.html", {"form": form})


@login_required
def authoradd(request):
    html = "authoradd.html"
    form = None

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(user=data["user"], bio=data["bio"])
            return render(request, "updated.html")
    else:
        form = AuthorAddForm()

    return render(request, html, {"form": form})


@login_required
def recipeadd(request):
    html = "recipeadd.html"
    form = None

    if request.method == "POST":
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"],
            )
            return render(request, "updated.html")

    else:
        form = RecipeAddForm()

    return render(request, html, {"form": form})


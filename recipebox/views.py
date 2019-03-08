from django.shortcuts import render, get_object_or_404
from .models import Author, Recipe
from .forms import AuthorAddForm, RecipeAddForm


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


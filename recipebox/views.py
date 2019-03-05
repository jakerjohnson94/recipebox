from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Author, Recipe


def recipe_list_view(request):
    recipes = Recipe.objects.all
    return render(request, "recipe_list.html", {"recipes": recipes})


def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def author_detail_view(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.filter(author=author_id)
    return render(
        request, "author_detail.html", {"author": author, "recipes": recipes}
    )

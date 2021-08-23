from django.shortcuts import render
from authors.models import Author


# Create your views here.
def authors_home_view(request):
    authors = Author.objects.all().order_by('lastname')
    context = {'authors': authors}
    return render(request, "authors/home.html", context)


from django.shortcuts import render


# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home/home.html", context)


def apps_view(request):
    context = {}
    return render(request, "home/apps.html", context)
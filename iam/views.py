from django.shortcuts import render


# Create your views here.
def iam_home_view(request):
    context = {}
    return render(request, "iam/home.html", context)


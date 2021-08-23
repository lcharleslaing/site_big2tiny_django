from django.urls import path
from iam.views import iam_home_view

urlpatterns = [
    path('', iam_home_view, name='iam_home'),
]
from django.urls import path
from authors.views import authors_home_view

urlpatterns = [
    path('', authors_home_view, name='authors_home'),
]

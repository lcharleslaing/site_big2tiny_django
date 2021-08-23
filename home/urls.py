# from django.contrib import admin
from django.urls import path
from home.views import home_view, apps_view

urlpatterns = [
    path('', home_view, name='home'),
    path('apps/', apps_view, name='apps'),
    # path('admin/', admin.site.urls),
]

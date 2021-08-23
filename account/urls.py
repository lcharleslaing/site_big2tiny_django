# from django.contrib import admin
from django.urls import path
from account.views import registration_view, account_home_screen_view, logout_view


urlpatterns = [
    path('', account_home_screen_view, name='account_home'),
    # path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
]

from django.contrib import admin
from django.urls import path
from plan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', todos),
    path('', loginView),
    path('logout/', logoutView),
]

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def hello_world(request):
    return HttpResponse("Hello, world. be41cf00 is the polls index.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello_world)
]

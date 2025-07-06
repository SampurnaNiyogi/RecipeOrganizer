from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi Django!!")


from .models import Users
user = Users(username="testuser", email="test@example.com", password_hash="hash")
user.save()
from django.http import Http404
from django.shortcuts import render,redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect
from . models import User
# LOGIN VIEW ENDPOINT

def login(response):

    return render(response, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass2']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password,email=email)
        user.save()
        return redirect("posts:post_home")
    return render(request, 'register.html')
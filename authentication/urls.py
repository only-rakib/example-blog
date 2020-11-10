from django.urls import path
from authentication.views import login, register
from posts.views import posts
urlpatterns = [
    path('login/', login,name="login"),
    path('register/', register, name="register"),
    path('post/', posts,name="post"),
]

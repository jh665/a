from django.views.generic import ListView
from .models import Post

class SingleAbout(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'single_pages/about_me.html'

class SingleHome(ListView):
    model = Post
    template_name = 'single_pages/home.html'



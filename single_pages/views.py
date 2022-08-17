from django.views.generic import ListView
from blog.models import Post

class SingleAbout(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'single_pages/about_me.html'

class SingleHome(ListView):
    recent_posts = Post.objects.order_by('-pk')[:3]
    model = Post
    template_name = 'single_pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(SingleHome, self).get_context_data()
        context['recent_posts'] = SingleHome.recent_posts
        return context



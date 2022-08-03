from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Categories
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    cat_list = Categories.objects.all()
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query)

            )
        return qs

def CategoryView(request, cats):
    if Categories.objects.filter(categoryname=cats).exists():
        category_posts = Post.objects.filter(category__categoryname=cats).order_by('-post_date')
        cat_list = Categories.objects.all()
        latestpost_list = Post.objects.all().order_by('-post_date')[:5]
        paginator = Paginator(category_posts, 4)
        page = request.GET.get('page')
        category_posts = paginator.get_page(page)
        return render(request, 'category_list.html', {'cats':cats, 'category_posts':category_posts, 'cat_list': cat_list, 'latestpost_list':latestpost_list})
    else:
        raise Http404


class PostDetailView(DetailView):
    model = Post
    cat_list = Categories.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    cat_list = Categories.objects.all()
    fields = ['title', 'email', 'gender' ,'birth_date', 'category', 'location' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    cat_list = Categories.objects.all()
    fields = ['title', 'email', 'gender', 'birth_date', 'category', 'location' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
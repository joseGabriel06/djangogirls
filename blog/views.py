from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .utils import LoginRequiredMixin
from .models import Post
from .forms import PostForm



class PostListView(ListView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PostForm

    def form_valid(self, form):
        furmulario = form.save(commit=False)
        furmulario.owner = self.request.user
        furmulario.save()
        self.object = furmulario
        return redirect('index')


class PostDetailView(DetailView):
    model = Post
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm



class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    form_class = PostForm

    def form_valid(self, form):
        furmulario = form.save(commit=False)
        furmulario.owner = self.request.user
        furmulario.save()
        self.object = furmulario
        return redirect('index')

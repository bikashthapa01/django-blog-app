from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy 
# Create your views here.

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class CreatePostView(CreateView):
	model = Post
	template_name = 'new_post.html'
	fields = '__all__'

class PostEditView(UpdateView):
	model = Post
	template_name = 'edit_post.html'
	fields = ['title','body']

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

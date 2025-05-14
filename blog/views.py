from .models import Post, Category
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post

class CategoryListView(ListView):
    model = Category

class PostDetailView(DetailView):
    model = Post

class PostsByCategoryView(ListView):
    model = Post
    template_name = 'blog/category_list.html'
    context_object_name = 'category_posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return self.category.get_posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = self.category
        return context


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):

        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            messages.error(self.request, "Debes iniciar sesión para poder publicar un post.")
            return redirect('admin:login')
        
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk}) + '?ok'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if form.instance.author != self.request.user:
                messages.error(self.request, "No tienes permisos para editar este post.")
                return redirect('blog:post_list')

            form.instance.author = self.request.user
        else:
            messages.error(self.request, "Debes iniciar sesión para poder editar el post.")
            return redirect('admin:login')

        return super().form_valid(form)



class PostDelete(DeleteView):
    model=Post
    success_url = reverse_lazy("blog:post_list")
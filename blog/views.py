from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:blogpost_list')

    def get_success_url(self):
        return reverse('blog:blogpost_detail', args=[self.object.slug])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')



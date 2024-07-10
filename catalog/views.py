from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, BlogPost


class ProductListView(ListView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'product_description', 'product_photo', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'product_description', 'product_photo', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class BlogPostListView(ListView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostDetailView(DetailView):
    model = BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published')
    success_url = reverse_lazy('catalog:blogpost_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published')
    success_url = reverse_lazy('catalog:blogpost_list')

    def get_success_url(self):
        return reverse('catalog:blogpost_detail', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blogpost_list')


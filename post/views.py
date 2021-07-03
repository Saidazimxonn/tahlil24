from django.shortcuts import render
from .models import Category, Tag, Posts, Author
from django.views.generic import TemplateView, ListView
# Create your views here.


class PostView(ListView):
    model = Posts
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        category = self.request.GET.get('category', 'None')
        print("------------------------------------",category)
        context = super(PostView, self).get_context_data(**kwargs)
        data_post = Posts.objects.all()
        auto = Author.objects.all()
        first_post = Posts.objects.first()
        two_post = Posts.objects.all()[1:3] 
        context['first_post'] = first_post
        context ['two_post'] = two_post
        context['data_post'] = data_post
        context['aut'] = auto
        return context
    
class CategoryVeiw(TemplateView):
    template_name = 'category.html'
    
    def get_context_data(self, **kwargs):
        id_c = self.kwargs['pk']
        print('===============================',id_c)
        context = super(CategoryVeiw, self).get_context_data(**kwargs)
        filter_category = Posts.objects.filter(category__id=id_c)
        context['filter_category'] = filter_category
        return context
        
        
    

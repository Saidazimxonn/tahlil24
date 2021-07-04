from django.shortcuts import render
from .models import Category, IpModel, Tag, Posts, Author
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect

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
        context = super(CategoryVeiw, self).get_context_data(**kwargs)
        filter_category = Posts.objects.filter(category__id=id_c)
        context['filter_category'] = filter_category
        
        return context
 
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


        
class PostDetail(DetailView):
    model = Posts
    template_name = 'blog-detail.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        print("*****************************************************",ip)
        if IpModel.objects.filter(ip=ip).exists():
            print('ip haqiqiqy')
            post_id = request.GET.get('post-id')
            print(post_id)
            blog = Posts.objects.get(pk=post_id)
            blog.views_post.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = request.GET.get('post-id')
            blog = Posts.objects.get(pk=post_id)
            blog.views_post.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(context)
            
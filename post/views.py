from .models import  IpModel, Posts, Author
from django.views.generic import TemplateView, ListView, DetailView, View
from django.shortcuts import redirect
from .helpers import create_email
from django.contrib import messages
from taggit.models import Tag
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import Q
# Create your views here.

# class TagMixin(object):
#     def get_context_data(self, **kwargs):
#         context = super(TagMixin, self).get_context_data(**kwargs)
#         context['tags'] = Tag.objects.all()
#         return context
    
    
#ListView 
class PostView(ListView):
    model = Posts
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        category = self.request.GET.get('category', 'None')
        context = super(PostView, self).get_context_data(**kwargs)
        data_post = Posts.objects.all()
        auto = Author.objects.all()
        posts = Posts.objects.all().order_by('-add_time')
    
        two_post = Posts.objects.all().order_by('-add_time')[1:3] 
        actual_post = Posts.objects.all().order_by('-views_post')[0:5]
        current_post1 = Posts.objects.filter(post_type='ACT').order_by('-add_time').first()
        current_post2 = Posts.objects.filter(post_type='ACT').order_by('-add_time')[1:3]
        # current_post = Posts.objects.filter(post_type='ACT')
        photo_posts = Posts.objects.filter(post_type='IMG').order_by('-add_time')[:4]
        video_posts= Posts.objects.filter(post_type='VED').order_by('-add_time')[:4]
        
        
    
        context['posts'] = posts
        context ['two_posts'] = two_post
        # context['data_post'] = data_post
        # context['aut'] = auto
        context['actual'] = actual_post
        context['current1'] = current_post1
        context['current2'] = current_post2
        # context['current'] = current_post
        context['photo_posts'] = photo_posts
        context['video_posts'] = video_posts
        
        return context
    
    
class CategoryVeiw(TemplateView):
    template_name = 'category.html'
    
    def get_context_data(self, **kwargs):
        id_c = self.kwargs['pk']
        actual_post = Posts.objects.all().order_by('-views_post')[0:5]
        context = super(CategoryVeiw, self).get_context_data(**kwargs)
        filter_category = Posts.objects.filter(category__id=id_c).order_by('id')[:2]
        context['actual'] = actual_post
        context['filter_category'] = filter_category
        context['category_id'] = id_c
        return context
    
    
class DynamicPostsLoad(View):
    
    @staticmethod
    def get(request, *args, **kwargs):
        last_post_id = request.GET.get('lastPostId')
        category_id = request.GET.get('categoryId')
        print(last_post_id)
        more_posts = Posts.objects.order_by('id').filter(pk__gt=int(last_post_id), category_id=category_id)\
            .values('id','title', 'image', 'content_mini', 'add_time' )[:2]
      
        if not more_posts:
            return JsonResponse({'data':False})
        data = []
        obj = dict()
        print(more_posts)
        for post in more_posts:
            print(post['id'])
            obj = {
                'id':post['id'],
                'title':post['title'],
                'image':post['image'],
                'content_mini':post['content_mini'],
                'add_time':post['add_time'],
             
                }
            data.append(obj)
        data[-1]['last_post'] = True
        return JsonResponse({'data':data})
    
    
    
    
    
class CategoryPostVeiw(ListView):
    model=Posts
    template_name = 'post_category.html'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
            id_c = self.kwargs['pk']
            context = super(CategoryPostVeiw, self).get_context_data(**kwargs)
            actual_post = Posts.objects.all().order_by('-views_post')[0:5]
            post_category = Posts.objects.all()      
            
            if int(id_c) == int(1):
                post_category = Posts.objects.filter(post_type='ACT')
            if int(id_c) == int(2):
                post_category = Posts.objects.filter(post_type='IMG')
            if int(id_c) == int(3):
                post_category = Posts.objects.filter(post_type='VED')  
            filter_post = post_category
            p= Paginator(filter_post,2)  # 3 posts in each page
            page_number = self.request.GET.get('page')
            try:
                page_obj = p.get_page(page_number)  # returns the desired page object
            except PageNotAnInteger:
                # if page_number is not an integer then assign the first page
                page_obj = p.page(1)
            except EmptyPage:
                # if page is empty then return last page
                page_obj = p.page(p.num_pages)
            context['number'] = id_c
            context['actual'] = actual_post
            context['page_obj'] = page_obj
            
            return context
        
class TagsView(ListView):
    model = Posts
    template_name = 'tags_category.html'
    
 
    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        tags = Posts.objects.all()
        filter_post=Posts.objects.filter(tags_new__slug=self.kwargs.get('tag_slug'))
        actual_post = Posts.objects.all().order_by('-views_post')[0:5]
        p= Paginator(filter_post,3)  # 3 posts in each page
        page_number = self.request.GET.get('page')
        try:
                page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
                # if page_number is not an integer then assign the first page
                page_obj = p.page(1)
        except EmptyPage:
             page_obj = p.page(p.num_pages)
             
        page_filter=page_obj
        context['actual'] = actual_post
        context['tags'] = page_filter
        
        return context

        
 
# Ip idress New client
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
    def get_context_data(self, **kwargs):
        actual_post = Posts.objects.all().order_by('-views_post')[0:3]
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['actual'] = actual_post
        
        return context
    

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        if IpModel.objects.filter(ip=ip).exists():
            post_id = request.GET.get('post-id')
            blog = Posts.objects.get(pk=post_id)
            blog.views_post.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = request.GET.get('post-id')
            blog = Posts.objects.get(pk=post_id)
            blog.views_post.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(context)
        
        
            
class ActionView(View):
    
    def post(self, request):
        post_request = request.POST
        print(post_request.get('action', None))
        actions = {
        
            'create_email' : create_email,
            
        }
        
        actions[self.request.POST.get('action', None)](post_request)
        messages.success(self.request, "Email Юборилди биз билан бўлганингиз учун ташаккур")
        return redirect('/')
    
    

    
class AboutWebSite(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super(AboutWebSite, self).get_context_data(**kwargs)
        actual_post = Posts.objects.all().order_by('-views_post')[0:5]
        context['actual'] = actual_post
        return context
    



class SearchView(View):
    
    
    def get(self, request):
        
        search_val = request.GET.get('search_val', 'all')
        elements = Posts.objects.all().in_bulk()
      
        if search_val !='all':
            elements = Posts.objects.filter(Q(title__icontains=search_val)|Q(content_mini__icontains=search_val)|Q(content__icontains=search_val)).in_bulk()
        posts = list()
        for post in elements.values():
            post_temp = dict(post.__dict__)
            post_temp['category'] = post.category.title
            try:
                post_temp.__delitem__('_state')
            except:
                pass
            posts.append(post_temp)
        data= {
                'posts':posts
            }
            
        return JsonResponse({'data':data})
         
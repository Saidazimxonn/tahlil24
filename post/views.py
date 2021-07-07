from .models import  IpModel, Posts, Author
from django.views.generic import TemplateView, ListView, DetailView, View
from django.shortcuts import redirect
from .helpers import create_email
from django.contrib import messages
from taggit.models import Tag
from django.http import JsonResponse
# Create your views here.
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
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
        print(Posts.objects.filter(category__id=id_c).values('id'))
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
            .values('id', 'user', 'category', 'title', 'image', 'content_mini', 
                    'content',  'add_time', 'post_type' )[:2]
      
        if not more_posts:
            return JsonResponse({'data':False})
        data = []
        obj = dict()
        print(more_posts)
        for post in more_posts:
            print(post['id'])
            obj = {
                'id':post['id'],
                'user':post['user'],
                'category':post['category'],
                'title':post['title'],
                'image':post['image'],
                'content_mini':post['content_mini'],
                'content':post['content'],
                'add_time':post['add_time'],
                'post_type':post['post_type'],
                }
            data.append(obj)
        data[-1]['last_post'] = True
        return JsonResponse({'data':data})
class CategoryPostVeiw(TemplateView):
    template_name = 'post_category.html'
  
    
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
        context['number'] = id_c
        context['actual'] = actual_post
        context['post_category'] = filter_post
        
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
    
class PostJsonView(View):
    
    def get(self, *args, **kwargs):
        pass
class AboutWebSite(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super(AboutWebSite, self).get_context_data(**kwargs)
        actual_post = Posts.objects.all().order_by('-views_post')[0:5]
        context['actual'] = actual_post
        return context
    

class TagsView(ListView):
    model = Posts
    template_name = 'tags_category.html'
    context_object_name = 'tags'
    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        tags = Posts.objects.all()
        actual_post = Posts.objects.all().order_by('-views_post')[0:5]
        context['actual'] = actual_post
        return context
    
    def get_queryset(self):
        return Posts.objects.filter(tags_new__slug=self.kwargs.get('tag_slug'))
        
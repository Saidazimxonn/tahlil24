from django.urls import path
from .views import PostView, CategoryVeiw, PostDetail ,CategoryPostVeiw, ActionView, PostJsonView, AboutWebSite, TagsView, DynamicPostsLoad


urlpatterns = [
    path('', PostView.as_view(), name='Post'),
    path('category/<int:pk>/', CategoryVeiw.as_view(), name='category'),
    path('blog_detail/<int:pk>/', PostDetail.as_view(), name='blog_detail'),
    path('post_detail/<int:pk>/' ,CategoryPostVeiw.as_view(), name='post_detail'),
    path('action/', ActionView.as_view(), name='action_view'),
    path('post-json/', PostJsonView.as_view(), name='post-json-view'),
    path('about-site/', AboutWebSite.as_view(), name='about-site'),
    path('tags/<slug:tag_slug>/', TagsView.as_view(), name='posts_by_tag'),
    path('load-more-posts/', DynamicPostsLoad.as_view(), name="load-more-posts"),
    
    
]


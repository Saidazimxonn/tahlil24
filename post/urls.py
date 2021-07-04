from django.urls import path
from .views import PostView, CategoryVeiw, PostDetail


urlpatterns = [
    path('', PostView.as_view(), name='Post'),
    path('category/<int:pk>/', CategoryVeiw.as_view(), name='category'),
    path('blog_detail/<int:pk>/', PostDetail.as_view(), name='blog_detail')
]


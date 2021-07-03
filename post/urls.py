from django.urls import path
from .views import PostView, CategoryVeiw


urlpatterns = [
    path('', PostView.as_view(), name='Post'),
    path('category/<int:pk>/', CategoryVeiw.as_view(), name='category')
]


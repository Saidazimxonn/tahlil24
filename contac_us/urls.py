from django.urls import path
from . import views
from .views import Add

urlpatterns = [
    path('', views.index, name='contact'),
    path('ad/', Add.as_view(), name='ad')

]


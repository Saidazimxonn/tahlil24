from django.shortcuts import render
from .forms import ContactForm
from post.models import Posts
from django.views.generic import TemplateView
# Create your views here.
from django.contrib import messages


def index(request):
    model = Posts
    actual_post = Posts.objects.all().order_by('-views_post')[0:5]
    
    form = ContactForm()
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form  = ContactForm()
            messages.success(request, "Контакт Юборилди биз билан бўлганингиз учун ташаккур")
            
    
    context = {'form':form,
               'actual':actual_post,}
    return render(request, 'contact.html', context)

class Add(TemplateView):
    template_name="ad.html"
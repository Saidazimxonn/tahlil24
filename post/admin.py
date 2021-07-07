from django.contrib import admin
from django.http import request
from .models import Category, Tag, Posts, Author, IpModel, Email
from django import forms
# Register your models here.


# class PostInline(admin.StackedInline):
#     def get_queryset(self, request):
#         return Posts.objects.filter(id__lt=0)
    
#     model= Posts
#     extra = 0
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Asosiy xabar")
    content_mini = forms.CharField(widget=CKEditorUploadingWidget(), label="Xabardan parcha 150 ta belgi")
    
    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'title']

    
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   list_display = ['id', 'title']
   list_display_links = ['id', 'title']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['id', 'category', 'user', 'title']
    list_filter = ['category', 'add_time','post_type']

    
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].queryset = Category.objects.filter(title='a')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user = request.user)
        return qs
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] =request.user.author.allowed_models
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(IpModel)
class IpModelAdmin(admin.ModelAdmin):
    pass
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass
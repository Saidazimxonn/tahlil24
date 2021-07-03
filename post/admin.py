from django.contrib import admin
from django.http import request
from .models import Category, Tag, Posts, Author
# Register your models here.


# class PostInline(admin.StackedInline):
#     def get_queryset(self, request):
#         return Posts.objects.filter(id__lt=0)
    
#     model= Posts
#     extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'title']

    
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'user', 'title']
    list_filter = ['category', 'add_time']
    
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

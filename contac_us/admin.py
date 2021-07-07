from django.contrib import admin
from .models import ConatacUS
# Register your models here.
@admin.register(ConatacUS)
class ContacUsAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import RegModel,Address,BlogModel
# Register your models here.

admin.site.register(RegModel)
admin.site.register(Address)
admin.site.register(BlogModel)
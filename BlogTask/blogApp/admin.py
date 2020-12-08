from django.contrib import admin
from blogApp.models import PublicBlogModel
from blogApp.models import PrivateBlogModel
# Register your models here.
admin.site.register(PublicBlogModel)
admin.site.register(PrivateBlogModel)

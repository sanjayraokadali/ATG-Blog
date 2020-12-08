from django.conf.urls import url
from blogApp import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogApp'

urlpatterns = [

    url('^$',views.RegistrationPage,name='registrationpage'),
    url('^LoginPage/$',views.LoginPage,name='loginpage'),
    url('^ViewBlogs/$',views.ViewBlogsPage,name='viewblogspage'),
    url('^CreateBlogPage/$',views.CreateBlogPage,name='createblogpage'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

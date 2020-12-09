from django.shortcuts import render
from blogApp.forms import UserRegistrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from blogApp.models import PublicBlogModel,PrivateBlogModel


# Create your views here.
def BasePage(request):

    return render(request,'blogApp/BasePage.html')

def SearchUserPage(request):

    if request.method == 'POST':

        blogs = PublicBlogModel.objects.all()

        search_user = request.POST.get('search_user')


        return render(request,'blogApp/SearchUserPage.html',{'blogs':blogs,'search_user':search_user})
    else:

        return HttpResponse('User Not Found')




def ViewBlogsPage(request):

    bag = True

    blogs = PublicBlogModel.objects.all()

    if PublicBlogModel.objects.count() == 0:
        bag = False
    else:
        bag =True

    return render(request,'blogApp/ViewBlogsPage.html',{'blogs':blogs,'bag':bag})

def PrivateBlogsPage(request):

    bag = True

    blogs = PrivateBlogModel.objects.all()
    pblog = PublicBlogModel.objects.all()


    if PrivateBlogModel.objects.count() == 0 and PublicBlogModel.objects.count() == 0:

        bag = False
    else:
        bag = True

    return render(request,'blogApp/PrivateBlogsPage.html',{'blogs':blogs,'bag':bag,'pblog':pblog})


def RegistrationPage(request):

    form = UserRegistrationForm()

    if request.method == 'POST':

        form = UserRegistrationForm(data = request.POST)
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if form.is_valid():

            if re_password == password:

                user = form.save()

                user.set_password(user.password)

                user.save()

                return BasePage(request)
            else:
                return render(request,'blogApp/RegistrationPage.html',{'user':form,'message':'passwords didnt match! Please Try Again!'})

    return render(request,'blogApp/RegistrationPage.html',{'user':form})

def CreateBlogPage(request):

    form = PublicBlogModel()

    if request.method == 'POST':

        username = request.POST.get('username')
        description = request.POST.get('description')
        pic = request.FILES.get('blog_pic')
        blog = request.POST.get('blog')

        type = request.POST.get('type')

        if type == 'Public':

            publicblog = PublicBlogModel.objects.create(username = username,
                                         description = description,
                                         pic = pic,
                                         blog = blog,
                                        )
            publicblog.save()

            return HttpResponseRedirect(reverse('blogApp:viewblogspage'))

        elif type == 'Private':

            privateblog = PrivateBlogModel.objects.create(username = username,
                                         description = description,
                                         pic = pic,
                                         blog = blog,
                                        )
            privateblog.save()

            return HttpResponseRedirect(reverse('blogApp:viewblogspage'))

    return render(request,'blogApp/CreateBlogPage.html',{'form':form})



def LoginPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:

            login(request,user)

            return HttpResponseRedirect(reverse('blogApp:viewblogspage'))

        else:

            return render(request,'blogApp/LoginPage.html',{'message':'Invalid Details, Please Try Again!'})

    return render(request,'blogApp/LoginPage.html')

@login_required
def LogOut(request):

    logout(request)

    return HttpResponseRedirect(reverse('basepage'))

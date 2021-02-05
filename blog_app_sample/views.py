from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from blog_app_sample.models import Blog
from django.core.files import File
from django.core.files.storage import FileSystemStorage
# Create your views here.


def user_registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username , password=password , email = email)
        return redirect(user_login)

    else: 
        return render(request , "user_registration.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect(user_view)
        else:
            return render(request , 'user_login.html')

    else:
        return render(request , 'user_login.html')


def user_view(request):
    user = request.user.id
    list_item = Blog.objects.all()
    return render(request , 'user_view.html',{"list_items" : list_item,"user":user}) 


def user_logout(request):
    auth.logout(request)
    return redirect("/")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username,password=password)

        if user.is_superuser:
            auth.login(request,user)
            return redirect(admin_view)
        else:
            return render(request , 'admin_login.html')

    else:
        return render(request , 'admin_login.html')


def admin_view(request):
    return render(request , 'admin_view.html')


def admin_view_save(request):
    if request.user.is_authenticated:


        title = request.POST.get("title")
        content = request.POST.get("content")
        content_image = request.FILES.get('content_image')


        blog = Blog(title1=title, content=content, content_image=content_image)
        blog.save()
        return redirect("admin_view")

    else:
        return render(request , 'admin_view.html')


def admin_logout(request):
    auth.logout(request)
    return redirect("admin_login")


from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from .models import author, category, article, comment

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import createForms, commentForms


# Create your views here.

def index(request):
    post = article.objects.all()
    scarch = request.GET.get('q')
    if scarch:
        post = post.filter(
            Q(title__icontains=scarch)
        )

    context = {
        "post": post
    }
    return render(request, "index.html", context)


def getAuthor(request, name):
    Post_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(author, name=Post_author.id)
    post = article.objects.filter(article_author=auth.id)
    context = {
        "auth": auth,
        "post": post
    }

    return render(request, "profile.html", context)


def getSingle(request, id):
    post = get_object_or_404(article, pk=id)
    first = article.objects.first()
    last = article.objects.last()
    getComment = comment.objects.filter( post= id)
    related = article.objects.filter(category=post.category).exclude(id=id)[:4]
    form = commentForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post = post
        instance.save()

    context = {
        "post": post,
        "first": first,
        "last": last,
        "related": related,
        "form": form,
        "comments": getComment
    }
    return render(request, "single.html", context)


def getTopic(request, name):
    cat = get_object_or_404(category, name=name)
    post = article.objects.filter(category=cat.id)
    return render(request, "category.html", {"post": post, "cat": cat})


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')

    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('index')
    return render(request, "login.html")


def getCreate(request):
    if request.user.is_authenticated:
        aut = get_object_or_404(author, name=request.user.id)
        form = createForms(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = aut
            instance.save();
            return redirect('index')
        context = {
            "form": form
        }
        return render(request, "create.html", context)
    else:
        return redirect("login")


def getUpdate(request, pid):
    if request.user.is_authenticated:
        aut = get_object_or_404(author, name=request.user.id)
        post = get_object_or_404(article, id=pid)
        form = createForms(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = aut
            instance.save();
            return redirect('profile')
        context = {
            "form": form
        }
        return render(request, "create.html", context)
    else:
        return redirect("login")


def getDelete(request, pid):
    if request.user.is_authenticated:
        aut = get_object_or_404(author, name=request.user.id)
        post = get_object_or_404(article, id=pid)
        post.delete()
        return redirect('profile')
    else:
        return redirect("login")


def getProfile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(author, name=request.user.id)
        post = article.objects.filter(article_author=user.id)
        context = {
            "post": post,
            "user": user
        }

        return render(request, "LoginProfie.html", context)
    else:
        return redirect("login")

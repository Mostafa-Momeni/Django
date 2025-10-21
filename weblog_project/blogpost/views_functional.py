from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import BlogPost,Comments
from .forms import BlogPostCommentForm
from .my_decorators import post_owner_required

def home(request):
    blog_posts = BlogPost.objects.all().order_by("-datetime_created")
    paginator = Paginator(blog_posts, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)

def recent_posts(request):
    blog_post = BlogPost.objects.all().order_by("-datetime_created")[:5]
    context = {"page_obj": blog_post}
    return render(request,"index.html",context)


# def detail_old(request, pk):
#     # post = BlogPost.objects.get(pk=pk)
#     post = get_object_or_404(BlogPost,pk=pk)
#     comments = Comments.objects.filter(post=post)
#     if request.method== "POST":
#         title = request.POST.get("title")
#         email = request.POST.get("email",None)
#         address = request.POST.get("address","")
#         city = request.POST.get("city","")
#         province = request.POST.get("province","")
#         zip_code = request.POST.get("zip_code","")
#         hide_name = request.POST.get("hide_name")
#         hide_name = True if hide_name else False
#         text = request.POST.get("text")
#         Comments.objects.create(
#             title=title,
#             email=email,
#             address=address,
#             city=city,
#             province=province,
#             zip_code=zip_code,
#             hide_name=hide_name,
#             comment=text,
#             post=post,
#         )          
#     context = {"post": post,"comments": comments}
#     return render(request,"detail.html",context)

def detail(request, pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost,pk=pk)
    # comments = Comments.objects.filter(post=post, state= Comments.STATE_CHOICES_APPROVD )
    comments = post.comments.filter(state= Comments.STATE_CHOICES_APPROVD )
    form = BlogPostCommentForm()
    if request.method== "POST":
        action = request.POST.get("action")
        if action == "comment":
            form = BlogPostCommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.post = post
                form.save()  
                form = BlogPostCommentForm()
        elif action == "like":
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
    context = {"post": post,"comments": comments,"form":form}
    return render(request,"detail.html",context)

@login_required
def add(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        desc = request.POST.get("description")
        picture = request.FILES.get("picture")
        new_post = BlogPost.objects.create(
            titel = title,
            description = desc,
            author = user,
            picture = picture
        )
        return redirect(new_post.get_absolute_url())
    context = {"page_name": "add"}
    return render(request,"add.html",context)

def test_func(user, *args, **kwargs):
    pk = kwargs.get("pk")
    post = get_object_or_404(BlogPost,pk=pk)
    if user.username=="admin":
        return True
    return user==post.author

@post_owner_required
def update(request, pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("description")
        picture = request.FILES.get("picture")
        post.titel = title
        post.description = desc
        post.picture = picture
        post.save()
        return redirect(post.get_absolute_url())
    context = {"post": post , "page_name": "update"}
    return render(request,"add.html",context)

@post_owner_required
def delete(request, pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    context = {"post": post}
    return render(request,"delete.html",context)



@login_required
def favorites(request):
    user = request.user
    blog_posts = user.blogpost_likes.all().order_by("-datetime_created")
    paginator = Paginator(blog_posts, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)


@login_required
def my_posts(request):
    user = request.user
    blog_posts = user.blogposts.all().order_by("-datetime_created")
    paginator = Paginator(blog_posts, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)
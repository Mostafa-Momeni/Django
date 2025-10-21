from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic  # for class based
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from .models import BlogPost, Comments
from .forms import BlogPostCommentForm


class BaseListView(generic.ListView):
    model = BlogPost
    template_name = "index.html"
    context_object_name = "post"
    paginate_by = 5


class Home(BaseListView):
    queryset = BlogPost.objects.all().order_by("-datetime_created")


class RecentPosts(BaseListView):
    paginate_by = 3
    queryset = BlogPost.objects.all().order_by("-datetime_created")[:5]


class Add(LoginRequiredMixin, generic.CreateView):
    model = BlogPost
    template_name = "add.html"
    context_object_name = "post"
    fields = ["titel", "description", "picture"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "add"
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        title = request.POST.get("title")
        desc = request.POST.get("description")
        picture = request.FILES.get("picture")
        new_post = BlogPost.objects.create(
            titel=title, description=desc, author=user, picture=picture
        )
        return redirect(new_post.get_absolute_url())


class Favorites(LoginRequiredMixin, BaseListView):
    def get_queryset(self):
        user = self.request.user
        return user.blogpost_likes.all().order_by("-datetime_created")


class MyPosts(LoginRequiredMixin, BaseListView):
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        return user.blogposts.all().order_by("-datetime_created")


class Detail(generic.DetailView):
    model = BlogPost
    template_name = "detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BlogPostCommentForm()
        post = self.get_object()
        # context["comments"] = Comments.objects.filter(post=post, state= Comments.STATE_CHOICES_APPROVD )
        context["comments"] = post.comments.filter(state=Comments.STATE_CHOICES_APPROVD)
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        post = self.get_object()
        if action == "comment":
            form = BlogPostCommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.post = post
                form.save()
                form = BlogPostCommentForm()
                messages.success(request,f"نظر شما با موفقیت دریافت شد و پس از تایید مدیریت در سایت بارگذاری خواهد شد.")
        elif action == "like":
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                messages.success(request,f"لایک پست { post.titel } با موفقیت حذف شد.")
            else:
                post.likes.add(request.user)
                messages.success(request,f"پست { post.titel } به لیست علاقه مندی های شما اضافه گردید.")
        return super().get(request, *args, **kwargs)


class Update(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = BlogPost
    template_name = "add.html"
    context_object_name = "post"
    fields = ["titel", "description", "picture"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "update"
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        title = request.POST.get("title")
        desc = request.POST.get("description")
        picture = request.FILES.get("picture")
        post.titel = title
        post.description = desc
        post.picture = picture
        post.save()
        return redirect(post.get_absolute_url())

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        # if user.username=="admin":  #جهت این که ادمین هم دسترسی به ویرایش تمامی پست ها داشته باشد
        #     return True
        return user == post.author


class Delete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = BlogPost
    context_object_name = "post"
    template_name = "delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user == post.author



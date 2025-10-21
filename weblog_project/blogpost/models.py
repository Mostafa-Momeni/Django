from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class BlogPost(models.Model):
    titel = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(to=get_user_model(),related_name="blogpost_likes",blank=True) # شیوه دوم
    author = models.ForeignKey(to=get_user_model(),on_delete=models.CASCADE,related_name="blogposts")
    picture = models.ImageField(upload_to="pictures/",blank=True,null=True)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.titel} --- {self.description[:10]}"

################## شیوه اول ################################
# class BlogPostLikes(models.Model):
#     post = models.ForeignKey(to=BlogPost,on_delete=models.CASCADE)
#     user = models.ForeignKey(to=get_user_model(),on_delete=models.CASCADE)
    
#     class Meta:
#         unique_together = ("post","user")   


    
    
class Comments(models.Model):
    CITY = (
        ("Tehran","تهران"),
        ("isfahan","اصفهان")
    )
    STATE_CHOICES_APPROVD  = "a"
    STATE_CHOICES_REJECTED = "r"
    STATE_CHOICES_PENDING  = "p"
    STATE_CHOICES = (
        ("a","تایید شده"),
        ("r","رد شده"),
        ("p","در انتظار تایید"),
    )
    name = models.CharField(max_length=255,verbose_name="نام")
    email = models.EmailField(null=True,blank=True,verbose_name="ایمیل")
    address = models.TextField(blank=True,verbose_name="آدرس")
    city = models.CharField(max_length=63,choices=CITY,blank=True,verbose_name="شهر")
    province = models.CharField(max_length=63,blank=True,verbose_name="استان")
    zip_code = models.CharField(max_length=11,blank=True,verbose_name="کد پستی")
    hide_name = models.BooleanField(default=True,verbose_name="عدم نمایش نام")
    comment = models.TextField(verbose_name="نظر")
    post = models.ForeignKey(to=BlogPost,on_delete=models.CASCADE,verbose_name="پست",related_name="comments")
    datetime_created = models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    datetime_modified = models.DateTimeField(auto_now=True,verbose_name="زمان آخرین ویرایش")
    state = models.CharField(max_length=1,choices=STATE_CHOICES ,default=STATE_CHOICES_PENDING,verbose_name="وضعیت کامنت")
    
    def __str__(self):
        return f"{self.comment[:20]}"
    
    
    
    
    
    
    "a","اداری و فروش",
    "b","پشتیبان تولید",
    "c","تولید",
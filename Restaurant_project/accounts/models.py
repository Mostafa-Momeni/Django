from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number  = models.CharField(max_length=11,null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)

############# AI Edite Code #################################
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
# from django.core.validators import MaxValueValidator, MinValueValidator
# from datetime import date

# class CustomUser(AbstractUser):
#     father_name = models.CharField(
#         max_length=255, 
#         null=True, 
#         blank=True, 
#         verbose_name="نام پدر"
#     )
    
#     national_code = models.CharField(
#         verbose_name="کد ملی",
#         max_length=10,
#         help_text="کد ملی ۱۰ رقمی کاربر را وارد کنید",
#         null=True,
#         blank=True, unique=True,
#     )
    
#     phone_number = PhoneNumberField(
#         null=True, 
#         blank=True, 
#         verbose_name="تلفن",
#         region='IR'  # اضافه کردن region برای ایران
#     )
    
#     birth_date = models.DateField(
#         verbose_name="تاریخ تولد",
#         blank=True,           # تغییر به True برای تست
#         null=True,            # تغییر به True برای تست
#         validators=[
#             MaxValueValidator(
#                 limit_value=date.today,
#                 message="تاریخ تولد نمی‌تواند در آینده باشد"
#             ),
#             MinValueValidator(
#                 limit_value=date(1299, 1, 1),
#                 message="تاریخ تولد باید بعد از سال 1299 باشد"
#             )
#         ],
#         help_text="تاریخ تولد کاربر را وارد کنید"
#     )
    
#     personal_number = models.PositiveIntegerField(verbose_name="کد پرسنلی")
    
#     def __str__(self):
#         return self.username or self.first_name or f"User {self.id}"
    
#     def calculate_age(self):
#         """محاسبه سن بر اساس تاریخ تولد"""
#         if not self.birth_date:
#             return None
#         today = date.today()
#         return today.year - self.birth_date.year - (
#             (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
#         )
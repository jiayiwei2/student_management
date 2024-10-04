from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # 名字
    last_name = models.CharField(max_length=100)   # 姓氏
    email = models.EmailField(unique=True)         # 电子邮件地址，设置为唯一
    date_of_birth = models.DateField()             # 出生日期
    enrollment_date = models.DateField()           # 入学日期
    grade = models.IntegerField()                  # 年级
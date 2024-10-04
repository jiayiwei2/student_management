from django.contrib import admin
from students.models import Student
# Register your models here.
# 自定义 ModelAdmin 类
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date')  # 定义列表显示的字段

# 注册 Student 模型和自定义的 StudentAdmin
admin.site.register(Student, StudentAdmin)


from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from .models import Student

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class StudentForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    grade = forms.IntegerField(
        validators=[
            MinValueValidator(1, message="Grade must be at least 1."),
            MaxValueValidator(12, message="Grade must not be greater than 12.")
        ]
    )

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

    def clean_email(self):
        email = self.cleaned_data['email']
        # 检查除当前实例外是否存在具有相同电子邮件的其他记录
        if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
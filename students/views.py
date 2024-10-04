# students/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


@login_required
def student_list(request):
    form = SearchForm(request.GET)
    students_list = Student.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        students_list = students_list.filter(first_name__icontains=query) | students_list.filter(last_name__icontains=query)

    paginator = Paginator(students_list, 2)  # 每页显示10名学生
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'students/student_list.html', {'students': students, 'form': form})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

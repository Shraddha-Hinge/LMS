from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def student_list(request):
    if not request.user.is_staff:
        return redirect('login')  
    students = Student.objects.all()
    return render(request, 'student_management/student_list.html', {
        'students': students,
        'base_template': 'base.html'
    })

@login_required
def student_add(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_management/student_form.html', {
        'form': form,
        'base_template': 'base.html'
    })

@login_required
def student_edit(request, id):
    if not request.user.is_staff:
        return redirect('login')
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_management/student_form.html', {
        'form': form,
        'base_template': 'base.html'
    })

@login_required
def student_delete(request, id):
    if not request.user.is_staff:
        return redirect('login')
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

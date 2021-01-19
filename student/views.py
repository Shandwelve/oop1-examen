from django.shortcuts import render, redirect
import statistics
from .services import get_students, add_student


def index(request):
    students = get_students(request.GET.get('order'), request.GET.get('direction'))
    marks_average = statistics.mean(map(lambda student: student.mark, students))
    order = {
        'order': request.GET.get('order') if request.GET.get('order') else 'name',
        'direction': request.GET.get('direction') if request.GET.get('direction') else 'ASC'
    }

    return render(request, 'student/list.html', {'students': students, 'order': order, 'marks_average': marks_average})


def add(request):
    add_student(request.POST.get('name'), request.POST.get('discipline'), request.POST.get('mark'))
    return redirect('index')


def add_from_file(request):
    content = str(request.FILES['uploadFile'].read())[2:-1].split(', ')
    add_student(content[0], content[1], int(content[2]))
    return redirect('index')

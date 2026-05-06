from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Q

# READ
def index(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(Q(name__icontains=query)| Q(age__icontains=query))
    else:
    
        students = Student.objects.all()
    return render(request, 'student1app/index.html', {'students': students})


# CREATE (ADD)
def add_student(request):
    form = StudentForm()
    
    if request.method == 'POST':
        

        form = StudentForm(request.POST,request.FILES)
        

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'student1app/add.html', {'form': form})


# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = StudentForm(instance=student)
    return render(request, 'student1app/update.html', {'form': form})


# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')



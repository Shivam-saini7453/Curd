
from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.shortcuts import render, redirect
from .models import Student

def index(request):
    
   
    return render(request, 'index.html')



def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        enrollment_date = request.POST.get('enrollment_date')
        course = request.POST.get('course')

        # Save to database
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            enrollment_date=enrollment_date,
            course=course
        )

        return redirect('success')  # Optional success page
    return render(request, 'student_create.html')



# this create view without mulple emailid add in databse 

# def student_create(request):
#     error_message = ''
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
        
#         # Check combinations
#         if Student.objects.filter(email=email, first_name=first_name, last_name=last_name).exists():
#             error_message = 'A student with this email and full name already exists.'
#         elif Student.objects.filter(email=email).exists():
#             error_message = 'A student with this email already exists.'
#         elif Student.objects.filter(first_name=first_name, last_name=last_name).exists():
#             error_message = 'A student with this full name already exists.'
#         else:
#             Student.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 age=request.POST.get('age'),
#                 enrollment_date=request.POST.get('enrollment_date'),
#                 course=request.POST.get('course'),
#             )
#             return redirect('success')  # or success page

#     return render(request, 'index.html', {'error_message': error_message})


def success_view(request):
    return render(request, 'success.html')  # or return HttpResponse("Success!")







def student_list(request):
    students = Student.objects.all()  # Fetch all student records
    return render(request, 'student_list.html', {'students': students})



def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        enrollment_date = request.POST.get('enrollment_date')

        # Only assign if enrollment_date is not empty
        if enrollment_date:
            student.enrollment_date = enrollment_date

        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')

    return render(request, 'student_update.html', {'student': student})



def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')



    

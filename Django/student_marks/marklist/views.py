from django.shortcuts import render
from django.contrib import messages
from marklist.models import Student
from marklist.forms import stform

############ Submit page #########
def mark_form(request):
    if request.method == 'POST':
        rno = request.POST['rnum']
        sn = request.POST['std']
        m1 = float(request.POST['m1'])
        m2 = float(request.POST['m2'])
        m3 = float(request.POST['m3'])
        tot = m1 + m2 + m3
        avg = tot / 3
        Student(roll_no=rno, name=sn, mark1=m1, mark2=m2, mark3=m3, total_mark=tot, avg_mark=avg).save(force_insert='__all__')
        messages.success(request, "Data of student " + sn + " is saved succesfully...")
        return render(request, 'mark_submit.html')
    else:
        return render(request, 'mark_submit.html')

############ Display page #########
def mark_view(request):
    print("BUAHAHAH")
    results = Student.objects.all().order_by('roll_no')
    return render(request, 'mark_data.html',{"Stud": results})

############## DELETE############
def delete(request, id):
    current_student = Student.objects.get(id=id)
    current_student.delete()
    results = Student.objects.all().order_by('roll_no')
    return render(request, "mark_data.html", {"Stud": results})

########## Edit page ##############
def markedit(request, id):
    current_student = Student.objects.get(id=id)
    return render(request, 'edit.html', {"Stud": current_student})

##############################
def update(request, id):
    current_student = Student.objects.get(id=id)
    form = stform(request.POST, instance=current_student)
    if form.is_valid():
        form.save()
        messages.success(request,"The Student Record is updated succesfully....")
        return render(request, 'mark_edit.html', {"Stud": current_student})
    else:
        return render(request, 'mark_edit.html')

########## View single student ##############
grade_index = { 95 : "O",
                90 : "A+",
                80 : "A",
                70 : "B",
                60 : "C",
                50 : "D",
                40 : "E"
            }
def view_student(request):
    if request.method == 'POST':
        rno = request.POST['rnum']
        current_student = Student.objects.get(roll_no=rno)
        grade = ''
        for x in grade_index:
            if current_student.avg_mark < 40:
                grade = "FAIL"
                break
            elif current_student.avg_mark >= x:
                grade = grade_index[x]
                break
        current_student.grade = grade
        return render(request, 'view_student.html', {"Stud": current_student})
    else:
        return render(request, 'view_student.html')

def indexpage(request):
    if 'add' in request.POST:
        rno = request.POST['rnum']
        sn = request.POST['std']
        m1 = float(request.POST['m1'])
        m2 = float(request.POST['m2'])
        m3 = float(request.POST['m3'])
        m4 = float(request.POST['m4'])
        tot = m1 + m2 + m3 + m4
        avg = tot / 4
        Student(roll_no=rno, name=sn, mark1=m1, mark2=m2, mark3=m3, mark4=m4, total_mark=tot, avg_mark=avg).save(force_insert='__all__')
        messages.success(request, "Data of student " + sn + " is saved succesfully...")
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

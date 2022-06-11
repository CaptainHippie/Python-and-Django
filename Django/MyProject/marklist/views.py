from django.shortcuts import render
from django.contrib import messages
from . models import Student
from . forms import stform

grade_index = { 95 : "O",
                90 : "A+",
                80 : "A",
                70 : "B",
                60 : "C",
                50 : "D",
                40 : "E" }

def get_tot_avg_grade(obj):
    grade = ''
    m1 = float(obj.mark1)
    m2 = float(obj.mark2)
    m3 = float(obj.mark3)
    m4 = float(obj.mark4)
    total = m1 + m2 + m3 + m4
    avg = total / 4
    for x in grade_index:
        if avg < 40:
            grade = "FAIL"
            break
        elif avg >= x:
            grade = grade_index[x]
            break
    obj.grade = grade
    obj.total_mark = total
    obj.avg_mark = avg
    return obj

############## ADD STUDENT DATA ##############
def add_student(request):
    if 'add' in request.POST:
        rno = request.POST['rnum']
        sn = request.POST['std']
        m1 = float(request.POST['m1'])
        m2 = float(request.POST['m2'])
        m3 = float(request.POST['m3'])
        m4 = float(request.POST['m4'])
        Student(roll_no=rno, name=sn, mark1=m1, mark2=m2, mark3=m3, mark4=m4).save(force_insert='__all__')
        messages.success(request, "Data of student " + sn + " is saved succesfully...")
        return render(request, 'mark_entry.html')
    else:
        return render(request, 'mark_entry.html')

############## VIEW ALL STUDENT DATA ##############
def view_all_data(request):
    results = Student.objects.all().order_by('roll_no')
    for current_student in results:
        current_student = get_tot_avg_grade(current_student)
    return render(request, 'view_all.html', {"Stud" : results})

############## SEARCH SINGLE STUDENT ##############
def search_student(request):
    if request.method == 'POST':
        rno = request.POST['rnum']
        current_student = Student.objects.get(roll_no = rno)
        current_student = get_tot_avg_grade(current_student)
        return render(request, 'search.html', {"Stud" : current_student})
    else:
        return render(request, 'search.html')

############## DELETE ############
def delete(request, id):
    current_student = Student.objects.get(id=id)
    current_student.delete()
    results = Student.objects.all().order_by('roll_no')
    return render(request, "view_all.html", {"Stud": results})

########## Edit page ##############
def markedit(request, id):
    current_student = Student.objects.get(id=id)
    return render(request, 'mark_entry.html', {"Stud": current_student})

##############################
def update(request, id):
    current_student = Student.objects.get(id=id)
    form = stform(request.POST, instance=current_student)
    if form.is_valid():
        form.save()
        messages.success(request,"The Student Record is updated succesfully....")
        return render(request, 'mark_entry.html', {"Stud": current_student})
    else:
        return render(request, 'mark_entry.html')
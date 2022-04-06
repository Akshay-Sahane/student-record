from django.shortcuts import render

from student.models import Student

# Create your views here.

from .forms import StudentForm
from django.shortcuts import redirect
from django.contrib import messages

#add new entry of student
def addstud(req):
    if req.method=='POST':
        form=StudentForm(data=req.POST)
        if form.is_valid():
            form.save()   #save in db
            messages.success(req,'student added.')
            return redirect('studlist')
        else:
            messages.error(req,'cant add student')
            context={'form':form}
            return render(req,'student/addstud.html',context)
    elif req.method=="GET":
        form=StudentForm()
        context={'form':form}
        return render(req,'student/addstud.html',context)

#display all student record
def studlist(req):
    slist=Student.objects.all()
    context={'slist':slist}
    return render(req,'student/studlist.html',context)

#delete student record
def deletestud(req,SId):
    stud=Student.objects.filter(SId=SId)[0]
    if req.method=='GET':
        context={'stud':stud}
        return render(req,'student/confirm_delete.html',context)
    elif req.method=='POST':
        stud.delete()
        messages.add_message(req,messages.SUCCESS,'student deleted.')
        return redirect('studlist')


#update student details
def editstud(req,SId):
        if req.method=='GET':
            stud=Student.objects.get(SId=SId)
            form=StudentForm(instance=stud)
            context={'form':form}
            return render(req,'student/addstud.html',context)
        if req.method=='POST':
            stud=Student.objects.get(SId=SId)
            form=StudentForm(data=req.POST,instance=stud)
            if form.is_valid():
                form.save()
                messages.success(req,'student record updated.')
                return redirect('studlist')
            else:
                context={'form':form}
                messages.error(req,"somethong went wrong try again")
                return render(req,'student/addstud.html',context)

#sort data in ascending order
def asc(req):
    slist=Student.objects.order_by('SName')
    context={'slist':slist}
    return render(req,'student/studlist.html',context)

#sort data in descending order
def desc(req):
    slist=Student.objects.order_by('-SName')
    context={'slist':slist}
    return render(req,'student/studlist.html',context)

#serach for a student record 
def studsearch(req):
    q=req.GET['q']
    slist=Student.objects.filter(SName__contains=q)
    context={'slist':slist}
    return render(req,'student/studlist.html',context)

from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.
def index(request):
    task=Task.objects.all()
    name='test'
    context={
        "tasks":task,
        "total_task":task.count(),
        "completed":task.filter(is_completed=True).count(),
        "in_completed":task.filter(is_completed=False).count(),
    }
    return render(request,'index.html',context)
 
def create_task(request):
    if request.method=="POST":
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        if title== "" or desc== "":
            context={}
            context['error']='title and discription are required'
            return render(request,'create.html',context)
            
        Task.objects.create(
            name=title,
            description=desc
        )
        return redirect('/')
     
    return render(request,'create.html')

def mark_completed(request,pk):
    try:
        task=Task.objects.get(pk=pk)
        task.is_completed=True
        task.save()
        return redirect('/')
    except Task.DoesNotExist:
        return HttpResponse("no such task exists")
   
def delete_task(request,pk):
    try:
        todo=Task.objects.get(pk=pk)
        todo.delete()
        return redirect('/')
    except Task.DoesNotExist:
        return HttpResponse("no such task exists")
    
def edit_task(request,pk):
    try:
        task=Task.objects.get(pk=pk)
        if request.method=="POST":
            new_title=request.POST.get('title')
            new_desc=request.POST.get('desc')
            task.title=new_title
            task.description=new_desc
            task.save()
            return redirect('/')
        context={
            'task':task
        }
        
        return render(request,'edit.html',context)
    except Task.DoesNotExist:
        return HttpResponse("no data exist")
from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.
def index(request):
    task=Task.objects.all()
    name='test'
    context={
        "tasks":task,
    }
    return render(request,'index.html',context)
 
def create_task(request):
    if request.method=="POST":
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        if title== "" and desc== "":
            context={}
            context['error']='title and discription are required'
            return render(request,'create.html',context)
            
        Task.objects.create(
            name=title,
            description=desc
        )
        return redirect('/')
     
    return render(request,'create.html')

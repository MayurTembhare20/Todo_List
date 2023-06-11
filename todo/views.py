from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from todo.models import todolist

# Create your views here.

def todo(request):
    if request.method=='POST':
        tile=request.POST.get('title')
        if tile:
            item=todolist(title=tile)
            item.save()
            
    data=todolist.objects.all()
    return render(request,'todolist.html',{'data': data})

def update(request,id):
    
    item=todolist.objects.get(id=id)  
    # item.check_status = not item.check_status
    item.check_status = True
    item.save()
    return HttpResponseRedirect(reverse('todo'))

def uncross(request,id):
    item=todolist.objects.get(id=id)  
    # item.check_status = not item.check_status
    item.check_status = False
    item.save()
    return HttpResponseRedirect(reverse('todo'))

def delete(request,id):
    item=todolist.objects.get(id=id)
    item.delete()

    return HttpResponseRedirect(reverse('todo'))


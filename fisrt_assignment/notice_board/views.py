from django.shortcuts import render,redirect
from .models import Notice

# Create your views here.
def notice_board(request ,id):
    notice_ = Notice.objects.get(pk=1) 
    title =  request.POST.get('title')
    text =  request.POST.get('text')
    contact_number = request.POST.get('contact number')
    notice = Notice(title=title,text= text,contact_number=contact_number)
    notice.save()
    return redirect(request, 'notice_board/notice.html' )







   
    # notice = Notice.objects.create(title=title,text=text,contact_number=contact)
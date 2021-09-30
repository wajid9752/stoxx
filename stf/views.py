from django.shortcuts import render,redirect
from stf.models import *
from stf.forms import *
from django.core.mail import send_mail
from datetime import date, timedelta,datetime
from time import gmtime, strftime
from django.contrib import messages
showtime = strftime("%H:%M:%S")
def home(request):
    #alll coure
    alls=Course.objects.all()
    #all services
    all_services=Services.objects.all()

    context={
        'couses':alls,
        'services':all_services,
    }

    return render(request, 'main/home.html',context)


def blog(request):
    blogs=Blog.objects.all()
    return render(request, 'blogs/blog.html',{'blogs':blogs}) 
    

def carrer(request):
    careers=Career.objects.all()
    return render(request, 'career/career.html',{'careers':careers}) 

def job_view(request ,pk):
    get_job=Career.objects.get(id=pk)
    context={'get_job':get_job,
            'form':ResumeForm()
                
    }
    return render(request, 'career/job_view.html',context)     





def contact(request):
    print(request)
    if request.GET:
        
        message_name=request.GET.get('message_name')
        meassage_email= request.GET.get('meassage_email')
        fullmessage=request.GET.get('message')
        
        
        send_mail(
			message_name, 
			fullmessage,
           
			'mawazid1051@gmail.com',
			[meassage_email],
			fail_silently=False,

        )
        
        return redirect('home')
    return redirect('home')


def resume(request):
    if request.method == 'POST':
        print("this is post request")
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request , 'Your request is submitted successfully')
            return redirect('carrer')
    return redirect('carrer')


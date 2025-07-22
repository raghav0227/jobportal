from django.shortcuts import render,HttpResponse
from home.models import Techmahindraapply,Datareg,Amazonapply,Microapply

def index(request):
    return render(request,'index.html')

def login(request):
    
    return render(request,'login.html')

def style(request):
    return render(request,'style.css')


def registerstyle(request):
    return render(request,'registerstyle.css')




def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        form = Datareg(name=name, email=email, password=password, phone=phone)
        form.save()
        #messages.success(request, 'Your message has been sent!')
        
    return render(request,'register.html')
  

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Do something with the uploaded file
        return render(request, 'upload_success.html', {'file_name': uploaded_file.name})
    




def microapply(request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            qualification = request.POST.get('qualification')
            salaryPackage = request.POST.get('salaryPackage')
            form = Microapply(name=name, email=email, phone=phone,qualification=qualification,salaryPackage=salaryPackage)
            form.save()
            #messages.success(request, 'Your message has been sent!')
            
        return render(request,'microapply.html')


def amazonapply(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        salaryPackage = request.POST.get('salaryPackage')
        form = Amazonapply(name=name, email=email, phone=phone,qualification=qualification,salaryPackage=salaryPackage)
        form.save()
        #messages.success(request, 'Your message has been sent!')
        
    return render(request,'amazonapply.html')

def techmahindraapply(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        salaryPackage = request.POST.get('salaryPackage')
        form = Techmahindraapply(name=name, email=email, phone=phone,qualification=qualification,salaryPackage=salaryPackage)
        form.save()
        #messages.success(request, 'Your message has been sent!')
    
    return render(request,'mahindratechapply.html')


def index(GET):
    return render(GET,'index.html')


def loginmain(request):
    return render(request,'loginmain.html')




def microabout(request):
    return render(request,'microabout.html')




def amazonabout(request):
    return render(request,'amazonabout.html')



def mahindratechabout(request):
    return render(request,'mahindratechabout.html')


def mahindratechapply(request):
    return render(request,'mahindratechapply.html')



def remote(request):
    return render(request,'remote.html')

def mnc(request):
    return render(request,'mnc.html')

def sales(request):
    return render(request,'sales.html')

def softit(request):
    return render(request,'softit.html')

def eng(request):
    return render(request,'engineering.html')

def marketing(request):
    return render(request,'marketing.html')

def about(request):
    return render(request,'aboutus.html')

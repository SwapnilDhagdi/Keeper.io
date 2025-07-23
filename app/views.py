from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from app.models import App

def app_method(request):
    return HttpResponse("Hello world",request)
# Create your views here.

def home(request):
    return redirect('/app')

def app(request):
    template=loader.get_template('index.html')
    return render(request,'index.html')

def students(request):
    mystudent=App.objects.all().values()
    template=loader.get_template("index.html")
    context={
        'students':mystudent,
    }
    return HttpResponse(template.render(context,request))

def form(request):
        if(request.method=='POST'):
            P_name=request.POST.get('Title')
            E_email=request.POST.get('Description')
            App(name=P_name,email=E_email).save()
        print(request)
        template=loader.get_template('index.html')
        context={
            'students':App.objects.all(),
        }
        return HttpResponse(template.render(context,request))
def post(request,id):
    print(id)

    todelete=App.objects.filter(id=id)  
    todelete.delete()         
    result=App.objects.all()
    context={
         'students':result,
    }
    # return HttpResponse(loader.get_template('output.html').render(context,request))
    return redirect('/app/form/')


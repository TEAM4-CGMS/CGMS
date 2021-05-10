from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'faq.html')

def thanku(request):
    return render(request,'thankyou_form.html')

def complainTracking(request):
    return render(request, 'complaint_tracking.html');

def check_status(request):
    return render(request,'enter_complaint_id.html')

def support(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        orderid=request.POST.get('orderid')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quetionstype=request.POST.get('quetionstype')
        subject=request.POST.get('subject')
        description=request.POST.get('description')
        Recommendation=request.POST.get('Recommendation')
        rate=request.POST.get('rate')
        #images=request.POST.get('images')
        
        contact.name=name
        contact.orderid=orderid
        contact.email=email
        contact.phone=phone
        contact.quetionstype=quetionstype

        contact.subject=subject
        contact.description=description
        contact.Recommendation=Recommendation
        contact.rate=rate
       # contact.images=images
        contact.save()
    
        return render(request,'thankyou_form.html')
   
    return render(request,'contact.html')



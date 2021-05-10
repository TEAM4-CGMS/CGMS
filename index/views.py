from django.shortcuts import render
from ticketinbox.models import Ticket
from login.models import Executive
from django.db.models import Q
from datetime import datetime,timedelta,time
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Aggregate,Avg


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        
        Unresolved = Ticket.objects.filter(Q(ticket_status='Unresolved')).count()
        Overdue = Ticket.objects.filter(Q(ticket_status='Overdue')).count()
        Closed = Ticket.objects.filter(Q(ticket_status='Closed')).count()
        Unassigned = Ticket.objects.filter(Q(ticket_status='Unassigned')).count()

        # data = Ticket.objects.filter(date_time_field__contains=datetime.date(2021, 4, 28))

        unhappy = Ticket.objects.filter(ticket_rating__lte=1).count()
        ok = Ticket.objects.filter(ticket_rating__range=(2,3)).count()
        happy = Ticket.objects.filter(ticket_rating__range=(4,5)).count()
        
        no_of_webform = Ticket.objects.filter(Q(source='Web-form')).count()
        no_of_email = Ticket.objects.filter(Q(source='Email')).count()
        no_of_socialmedia = Ticket.objects.filter(Q(source='Social-media')).count()

        avg_responce_time = Executive.objects.all().aggregate(Avg('avg_response'))
        avg_resolve_time = Executive.objects.all().aggregate(Avg('avg_resolution'))

        avg_resp = avg_responce_time.get("avg_response__avg")
        avg_resolve = avg_resolve_time.get("avg_resolution__avg")

        today = datetime.now()

        # data = Ticket.objects.all()
        # print(data)
        # print(avg_responce_time.get("avg_resolution__avg"))

        dashboard_data = {
            "unresolved":Unresolved,
            "overdue":Overdue,
            "closed": Closed,
            "unassigned":Unassigned ,
            "no_of_webform":no_of_webform,
            "no_of_email":no_of_email,
            "no_of_socialmedia":no_of_socialmedia,
            "avg_resolve_time":avg_resolve,
            "avg_responce_time":avg_resp,
            "happy":happy,
            "ok":ok,
            "unhappy":unhappy,
            "today":today,
            "name":request.user
            
        }
        return render(request,'dashboard.html', dashboard_data)
    else:
        return redirect('/')


        # return HttpResponseRedirect('/loginPage/') 
       # return redirect('loginPage')



# executive_profile view
def profile(request):
    # executive_data = Executive.objects.all().filter(executive_email='kunalnag99@gmail.com')
    executive_data = Executive.objects.filter(executive_email=request.user.email)
    print(executive_data)
    # var = executive_data.get('executive_name')
    # print(var)
    # for i in executive_data:
        # print(i)
    return render(request,'executive_profile.html',{'executive_data':executive_data})


def editprofile(request):
    return render(request,'edit_profile_form.html')

def logoutProfile(request):
    logout(request)
    return render(request,'logout_form.html')

def ticketinbox(request):


    return render(request,'TicketInbox.html',)
from django.shortcuts import render
from ticketinbox.models import Ticket
from login.models import Executive
from django.db.models import Q
import datetime
from datetime import date,timedelta,time
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Club
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models import Avg,Sum
from statistics import mean
# Create your views here.
def Charts(request):
    return render(request, 'Charts.html')
     
def chart(request):
    today=date.today()

    Email_today=Ticket.objects.filter(Q(created_on__day=today.day,source='Email')).count()
    Webform_today=Ticket.objects.filter(Q(created_on__day=today.day,source='Web-form')).count()
    Socialmedia_today=Ticket.objects.filter(Q(created_on__day=today.day,source='Social-media')).count()

    Email_weekly=Ticket.objects.filter(Q(created_on__month=today.month,source='Email')).count()
    Webform_weekly=Ticket.objects.filter(Q(created_on__month=today.month,source='Web-form')).count()
    Socialmedia_weekly=Ticket.objects.filter(Q(created_on__month=today.month,source='Social-media')).count()

    Email_monthly=Ticket.objects.filter(Q(created_on__month=today.month,source='Email')).count()
    Webform_monthly=Ticket.objects.filter(Q(created_on__month=today.month,source='Web-form')).count()
    Socialmedia_monthly=Ticket.objects.filter(Q(created_on__month=today.month,source='Social-media')).count()

    Email_yearly=Ticket.objects.filter(Q(created_on__year=today.year,source='Email')).count()
    Webform_yearly=Ticket.objects.filter(Q(created_on__year=today.year,source='Web-form')).count()
    Socialmedia_yearly=Ticket.objects.filter(Q(created_on__year=today.year,source='Social-media')).count()

    traffic_data={
        "Email_today":Email_today,
        "Webform_today":Webform_today,
        "Socialmedia_today":Socialmedia_today,
        "Email_weekly":Email_weekly,
        "Webform_weekly":Webform_weekly,
        "Socialmedia_weekly":Socialmedia_weekly,
        "Email_monthly":Email_monthly,
        "Webform_monthly":Webform_monthly,
        "Socialmedia_monthly":Socialmedia_monthly,
        "Email_yearly":Email_yearly,
        "Webform_yearly":Webform_yearly,
        "Socialmedia_yearly":Socialmedia_yearly
    }
    return render(request,'base.html',traffic_data)


def TicketStatistics(request):
    today=date.today()
    
    High_today=Ticket.objects.filter(Q(created_on__day=today.day,ticket_priority='High')).count()
    Medium_today=Ticket.objects.filter(Q(created_on__day=today.day,ticket_priority='Medium')).count()
    Low_today=Ticket.objects.filter(Q(created_on__day=today.day,ticket_priority='Low')).count()

    High_weekly=Ticket.objects.filter(Q(created_on__month=today.month,ticket_priority='High')).count()
    Medium_weekly=Ticket.objects.filter(Q(created_on__month=today.month,ticket_priority='Medium')).count()
    Low_weekly=Ticket.objects.filter(Q(created_on__month=today.month,ticket_priority='Low')).count()


    High_monthly=Ticket.objects.filter(Q(created_on__month=today.month,ticket_priority='High')).count()
    Medium_monthly=Ticket.objects.filter(Q(created_on__month=today.month,ticket_priority='Medium')).count()
    Low_monthly=Ticket.objects.filter(Q(created_on__month=today.month,ticket_priority='Low')).count()

    High_yearly=Ticket.objects.filter(Q(created_on__year=today.year,ticket_priority='High')).count()
    Medium_yearly=Ticket.objects.filter(Q(created_on__year=today.year,ticket_priority='Medium')).count()
    Low_yearly=Ticket.objects.filter(Q(created_on__year=today.year,ticket_priority='Low')).count()


    ticketStatistics_data={
        "High_today":High_today,
        "Medium_today":Medium_today,
        "Low_today":Low_today,
        "High_weekly":High_weekly,
        "Medium_weekly":Medium_weekly,
        "Low_weekly":Low_weekly,
        "High_monthly":High_monthly,
        "Medium_monthly":Medium_monthly,
        "Low_monthly":Low_monthly,
        "High_yearly":High_yearly,
        "Medium_yearly":Medium_yearly,
        "Low_yearly":Low_yearly,
    }

    return render(request,'TicketStatistics.html',ticketStatistics_data)  

def Average_Ticket_Response(request):
    return render(request, 'Average_Ticket_Response.html')


def Average_Ticket_Resolution(request):
    return render(request, 'Average_Ticket_Resolution.html')

def customerRating(request):
    today=date.today()
    
    Happy_today=Ticket.objects.filter(created_on__day=today.day,ticket_rating__range=(4,5)).count()
    Neutral_today=Ticket.objects.filter(created_on__day=today.day,ticket_rating__range=(2,3)).count()
    Sad_today=Ticket.objects.filter(created_on__day=today.day,ticket_rating__lte=1).count()

    Happy_weekly=Ticket.objects.filter(created_on__day=today.day,ticket_rating__range=(4,5)).count()
    Neutral_weekly=Ticket.objects.filter(created_on__day=today.day,ticket_rating__range=(2,3)).count()
    Sad_weekly=Ticket.objects.filter(created_on__day=today.day,ticket_rating__lte=1).count()

    Happy_monthly=Ticket.objects.filter(created_on__month=today.month,ticket_rating__range=(4,5)).count()
    Neutral_monthly=Ticket.objects.filter(created_on__month=today.month,ticket_rating__range=(2,3)).count()
    Sad_monthly=Ticket.objects.filter(created_on__month=today.month,ticket_rating__lte=1).count()

    Happy_yearly=Ticket.objects.filter(created_on__year=today.year,ticket_rating__range=(4,5)).count()
    Neutral_yearly=Ticket.objects.filter(created_on__year=today.year,ticket_rating__range=(2,3)).count()
    Sad_yearly=Ticket.objects.filter(created_on__year=today.year,ticket_rating__lte=1).count()

    CustomerRating_data={
        "Happy_today":Happy_today,
        "Neutral_today":Neutral_today,
        "Sad_today":Sad_today,
        "Happy_weekly":Happy_weekly,
        "Neutral_weekly":Neutral_weekly,
        "Sad_weekly":Sad_weekly,
        "Happy_monthly":Happy_monthly,
        "Neutral_monthly":Neutral_monthly,
        "Sad_monthly":Sad_monthly,
        "Happy_yearly":Happy_yearly,
        "Neutral_yearly":Neutral_yearly,
        "Sad_yearly":Sad_yearly,
        
    }
    return render(request,'customerRating.html',CustomerRating_data)
    
def auto(request):
    today=date.today()

    Automatic_today=Ticket.objects.filter(Q(created_on__day=today.day,process='Automatic')).count()
    Manual_today=Ticket.objects.filter(Q(created_on__day=today.day,process='Manual')).count()

    Automatic_weekly=Ticket.objects.filter(Q(created_on__month=today.month,process='Automatic')).count()
    Manual_weekly=Ticket.objects.filter(Q(created_on__month=today.month,process='Manual')).count()
    
    Automatic_monthly=Ticket.objects.filter(Q(created_on__month=today.month,process='Automatic')).count()
    Manual_monthly=Ticket.objects.filter(Q(created_on__month=today.month,process='Manual')).count()

    Automatic_yearly=Ticket.objects.filter(Q(created_on__year=today.year,process='Automatic')).count()
    Manual_yearly=Ticket.objects.filter(Q(created_on__year=today.year,process='Manual')).count()


    automation_data={
        "Automatic_today":Automatic_today,
        "Manual_today":Manual_today,
        "Automatic_weekly":Automatic_weekly,
        "Manual_weekly":Manual_weekly,
        "Automatic_monthly":Automatic_monthly,
        "Manual_monthly":Manual_monthly,
        "Automatic_yearly":Automatic_yearly,
        "Manual_yearly":Manual_yearly

    }

    return render(request,'auto.html',automation_data)



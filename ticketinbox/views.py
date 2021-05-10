from django.shortcuts import render
from .models import Ticket
from .models import Product
from django.db.models import Q
from index.models import Customer
# Create your views here.
def ticketinbox(request):
    ticket=Ticket.objects.all().select_related('assigned_to')
    for i in ticket:
        print(i.title,i.assigned_to.executive_name)
    return render(request,'TicketInbox.html',{'ticket':ticket})

def profileDetail(request):
    #all details will be passed from here
    if request.user.is_authenticated:
        Unresolved = Ticket.objects.all().select_related('customer_id')
        assignment=Ticket.objects.all().select_related('assigned_to')
        #Unresolved = Ticket.objects.all().values('id','id','customer_id')
        #Ticket.objects.select_related(customer_id=Customer.id)
        #Unresolved = Ticket.objects.filter(Q(id=customer_id))
       # for unresolved in Unresolved:
         #   print(unresolved.customer_id.customer_name)
       #     print(unresolved.customer_id.customer_email)
        #    print(unresolved.customer_id.customer_contact)
        print(Unresolved)
#         context_name = {
#             "name":Unresolved.customer_id.customer_name,
#             "mail":Unresolved.customer_id.customer_email,
#             "contact":Unresolved.customer_id.customer_contact
# }
        #for i in assignment:
         #   print(i.assigned_to.executive_name)

    else:
        return HttpResponseRedirect('/loginPage/')


    # return render(request,'ticket_details.html',context_name)
    return render(request,'ticket_details.html')


def ReplyTicket(request):
    return render(request,'reply_ticket_form.html')
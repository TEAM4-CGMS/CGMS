from . import views
from django.urls import path

urlpatterns = [
    path('',views.ticketinbox,name='ticketinbox'),
    path('detail',views.profileDetail,name='profileDetail'),
    path('replay',views.ReplyTicket,name='ReplyTicket'),

]
from django.db import models
from django.utils.timezone import now
from datetime import datetime
from index.models import Customer
from login.models import Executive

# Create your models here.

class Ticket(models.Model):
    status = (
        ('Closed','Closed'),
        ('Unassigned','Unassigned'),
        ('Unresolved','Unresolved'),
        ('Overdue','Overdue')
    )

    src = (
        ('Email','Email'),
        ('Web-form','Web-form'),
        ('Social-media','Social-media')
    )

    process = (
        ('Automatic','Automatic'),
        ('Manual','Manual')
    )

    id = models.AutoField(primary_key=True,max_length=10)
    title =models.CharField(max_length=200)
    ticket_type=models.CharField(max_length=200)
    ticket_priority=models.CharField(max_length=10)
    source=models.CharField(max_length=30,choices=src)
    ticket_status=models.CharField(max_length=30,choices=status)
    assigned_dep=models.CharField(max_length=30,null=True)
    created_on=models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    due_date=models.DateTimeField(auto_now_add=False, null=True, blank=True)
    assigned_to=models.ForeignKey(Executive,max_length=10,null=True,on_delete=models.SET_NULL)
    ticket_rating=models.CharField(max_length=10,null=True)
    solution=models.CharField(max_length=200,null=True)
    customer_id = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    process=models.CharField(max_length=20,null=True,choices=process)


    def __str__(self):
        return self.title


class Product(models.Model):
    ctgr=(
        ('clothing','clothing'),
        ('accessories','accessories'),
        ('footwear','footwear')

    )
    id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=200)
    product_catogary=models.CharField(max_length=200,choices=ctgr)
    def _str_(self):
        return self.product_name





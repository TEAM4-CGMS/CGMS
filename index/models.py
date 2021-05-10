from django.db import models



# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True,max_length=10)
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()
    customer_contact=models.IntegerField()
    customer_address=models.CharField(max_length=300,null=True)
    issue=models.CharField(max_length=300,null=True)
    nO_of_issues=models.IntegerField()


    def __str__(self):
        return self.customer_name
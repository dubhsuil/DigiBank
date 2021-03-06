from django.db import models
from customer_site.models import Customer
from django.utils import timezone


# Create your models here.
class DDRequest(models.Model):
    requester = models.ForeignKey(Customer,
                                  on_delete=models.DO_NOTHING)
    rec_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    address_st = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_zip = models.IntegerField()
    rec_phone = models.IntegerField()
    send_date = models.DateField(default=timezone.now)
    payable_date = models.DateField(default=timezone.now)
    message = models.CharField(max_length=240)
    account_from = models.ForeignKey("Account",
                                     on_delete=models.DO_NOTHING)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.requester) + ": " + str(self.amount)

class CheckRequest(models.Model):
    account = models.ForeignKey("Account",
                                on_delete=models.DO_NOTHING)
    address_st = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_zip = models.IntegerField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.account)


class Account(models.Model):
    # Account Model included by<kashif> to utilize Account details
    accountNum = models.IntegerField()
    routingNum = models.IntegerField()
    balance = models.FloatField(max_length=20)
    acntType = models.CharField(max_length=15)
    owner = models.ForeignKey(Customer, null=False,
                              on_delete=models.CASCADE)

    def __str__(self):
        return str(self.accountNum)


class Transactions(models.Model):
    # Transaction Model included by<kashif> to utilize Transaction details
    accntTo = models.IntegerField(null=False)
    accntFrom = models.ForeignKey(Account, null=False,
                                  on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=timezone.now)
    toRoutingNo=models.IntegerField(null=False)
    amount = models.FloatField(max_length=15)
    transferDesc = models.CharField(max_length=200)

    def __str__(self):
        return str(self.accntFrom) + " to " + str(self.accntTo)


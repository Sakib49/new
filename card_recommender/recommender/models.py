from django.db import models

# Create your models here.



class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default =False)


class Card(models.Model):
    card_name  = models.CharField(max_length=150)
    bank_name  = models.CharField(max_length=150)                  
    url    = models.CharField(max_length=300)                                   
    card_type = models.CharField(max_length=100)                   
    interest_rate = models.FloatField(null=True,blank=True)
    cash_withdrawal_limit_per_transaction = models.FloatField(null=True,blank=True)
    cash_withdrawal_limit_per_day = models.FloatField(null=True,blank=True)
    max_credit_limit = models.FloatField(null=True,blank=True)
    international_transaction_available = models.BooleanField(default =False)   
    balance_transfer_available  = models.BooleanField(default =False)               
    dual_currency  = models.BooleanField(default =False)                            
    reward_supplementary_card = models.BooleanField(default =False)                  
    reward_airport_lounge     = models.BooleanField(default =False)                 
    reward_cashback_available = models.BooleanField(default =False)                 
    reward_luxary_resort_hotel= models.BooleanField(default =False)                 
    reward_insurance_plan     = models.BooleanField(default =False)                 
    reward_travel_benefits    = models.BooleanField(default =False)                 
    reward_fine_dining        = models.BooleanField(default =False)                 
    reward_buffet_discount    = models.BooleanField(default =False)                 
    reward_medical_discount   = models.BooleanField(default =False)                 
    reward_shopping           = models.BooleanField(default =False)                 
    reward_airlines_ticket    = models.BooleanField(default =False)                 
    reward_point_program      = models.BooleanField(default =False)                 
    reward_emi_available      = models.BooleanField(default =False)                 
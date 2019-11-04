from django.db import models

# Create your models here.


# Create your models here.
class StatusCallBack(models.Model):
    account_sid = models.CharField(max_length=255, default='')
    caller_name = models.CharField(max_length=255, default='')
    duration = models.CharField(max_length=255, default='')
    # end_time = models.DateTimeField()
    caller = models.CharField(max_length=255, default='')
    # price = models.DecimalField(max_digits=100)

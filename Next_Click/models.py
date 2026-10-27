from django.db import models
import datetime

class OTP(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    expiry = models.DateTimeField()

    def is_valid(self):
        return datetime.datetime.now() < self.expiry
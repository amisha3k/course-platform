from django.db import models

class Email(models.Model):
    email=models.EmailField(unique=True)
    timestamp=models.DateTimeField(auto_now_add=True)

class EmailVerifiactionEvent(models.Model):   
    email=models.ForeignKey(Email,on_delete=models.SET_NULL,null=True)
    email=models.EmailField() #
    #token
    attempts=models.IntegerField(default=0)
    expired_at=models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )
    expired = models.BooleanField(default=False)
    expired_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )
    timestamp=models.DateTimeField(auto_now_add=True)



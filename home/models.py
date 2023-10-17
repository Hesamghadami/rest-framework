from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.name
    


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email



# Create your models here.

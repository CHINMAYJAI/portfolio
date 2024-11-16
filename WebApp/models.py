from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=122)
    reason_to_contact = models.TextField()
    date = models.DateField()

    # String representation to display the user's name
    def __str__(self):
        return self.name

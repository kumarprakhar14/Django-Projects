from django.db import models

# Create your models here.

# makemigration -> create changes and store in a file
# migrate -> apply pending changes to the database created by database


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return "This Information is not displayable"


class Info(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    major = models.CharField(max_length = 200)
    faculty = models.CharField(max_length = 200)
    account = models.ForeignKey(Account, on_delete = models.CASCADE)

    def __str__(self):
        return str("{}\n{}\n{}\n{}\n").format(self.first_name, self.last_name, self.major, self.faculty)

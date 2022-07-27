from django.db import models


# Create your models here.
class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    interest = models.ForeignKey(Interest, models.CASCADE)

    def __str__(self):
        return f'{self.interest} - {self.name}'


class College(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch,models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField(default=50)
    number = models.CharField(max_length= 15)
    password = models.CharField(max_length= 500)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
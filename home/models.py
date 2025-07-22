from django.db import models

# Create your models here.

class Techmahindraapply(models.Model):
     name = models.CharField(max_length=122)
     email = models.CharField(max_length=122)
     phone = models.CharField(max_length=12,primary_key=True)
     qualification = models.CharField(max_length=122)
     salaryPackage = models.CharField(max_length=122)


class Microapply(models.Model):
     name = models.CharField(max_length=122)
     email = models.CharField(max_length=122)
     phone = models.CharField(max_length=12,primary_key=True)
     qualification = models.CharField(max_length=122)
     salaryPackage = models.CharField(max_length=122)


class Amazonapply(models.Model):
     name = models.CharField(max_length=122)
     email = models.CharField(max_length=122)
     phone = models.CharField(max_length=12,primary_key=True)
     qualification = models.CharField(max_length=122)
     salaryPackage = models.CharField(max_length=122)
     
class Datareg(models.Model):
     name = models.CharField(max_length=122)
     email = models.CharField(max_length=122)
     password = models.CharField(max_length=50)
     phone = models.CharField(max_length=12,primary_key=True)


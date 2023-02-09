from django.db import models

class Member(models.Model):
     fname = models.CharField(max_length=50, null= True)
     lname = models.CharField(max_length=100, null=True)
     email = models.EmailField(max_length=100, null=True)
     passwd = models.CharField(max_length=50, null=True)

     def __str__(self):
          return self.fname + ' ' + self.lname

class Orgazniation(models.Model):
    orgName = models.CharField(max_length=50, null=True)
    def __str__(self):
         return self.orgName
    
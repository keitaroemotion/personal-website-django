from django.db import models

class User(models.Model):
    pass

class Credential(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    email    = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Profile(models.Model):
    firstName    = models.CharField(max_length=100)
    lastName     = models.CharField(max_length=100)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=200)
    photo        = models.CharField(max_length=100) # physical path or S3

#
# skill tag
#
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name    = models.CharField(max_length=50)
    level   = models.CharField(max_length=100) # (ELEMENTARY | MIDDLE | ADVANCED)
    years   = models.IntegerField(default=0, max_length=50)

class Company(models.Model):
    name           = models.CharField(max_length=50)
    description    = models.CharField(max_length=2000)

class Role(models.Model):
    company        = models.ForeignKey(Company, on_delete=models.CASCADE)
    title          = models.CharField(max_length=50)
    description    = models.CharField(max_length=2000)
    salaryMin      = models.IntegerField(default=0)
    salaryMax      = models.IntegerField(default=0)
    employmentType = models.CharField(max_length=50)

class CredentialForCompany(models.Model):
    company  = models.ForeignKey(Company, on_delete=models.CASCADE)
    email    = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

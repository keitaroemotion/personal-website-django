from django.db import models

class User(models.Model):
    pass

class Credential(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    email    = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)   # there should be minimum length

class Profile(models.Model):
    firstName    = models.CharField(max_length=100)
    lastName     = models.CharField(max_length=100)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=200)
    photo        = models.CharField(max_length=100) # physical path or S3

class Payment(models.Model):
    profile         = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bitCoinAddress  = models.CharField(max_length=100)

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name    = models.CharField(max_length=50)
    level   = models.CharField(max_length=100) # (ELEMENTARY | MIDDLE | ADVANCED)
    years   = models.IntegerField(default=0, max_length=50)

class Replutation(models.Model):
    pass

class Score(models.Model):
    reputation = models.ForeignKey(Replutation, on_delete=models.CASCADE)
    count      = models.IntegerField(default=0, max_length=10)
    comment    = models.CharField(max_length=200)

    



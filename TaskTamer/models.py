from django.db import models
from django.contrib.auth.models import User



class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #pip install pillow
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)


class Tasks(models.Model):
    task_title = models.CharField(max_length=200, null=True)
    task_description = models.CharField(max_length=200, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True) #
    challenge = models.BooleanField(default=False) # ewentualne zmiany
    #every tasks cost 1 point
    #every challenge cost 2 point


    def __str__(self):
        return self.task_title

class User_Tasks(models.Model):
    date_create = models.DateTimeField(auto_now_add=True, null=True) #
    point_earned = models.PositiveIntegerField(default=1)
    date_deadline = models.DateTimeField(auto_now_add=False)
    task_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, null=True, on_delete=models.CASCADE)




class Rewards(models.Model):
    rewards_name = models.CharField(max_length=200, null=True)
    rewards_cost = models.IntegerField()

    def __str__(self):
        return self.rewards_name

class Acivement(models.Model):
    rewards = models.ForeignKey(Rewards, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
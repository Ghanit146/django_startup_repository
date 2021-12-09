from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Idea(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)  # User is specified for this idea creation
     title = models.CharField(max_length=100)
     problem = models.TextField(max_length=200)
     solution = models.TextField(max_length=200)
     business_model = models.TextField(blank=True) #The field can be left blank
     market = models.TextField(blank=True)
     created = models.DateTimeField(auto_now_add=True) #Date and time of the edit or created can't be changed
     edited = models.DateTimeField(auto_now_add=True,null=True,blank=True) #when user edits the fields date and time will be recorded
     logs = models.TextField(blank=True)
     phase = models.TextField(max_length=50,blank=True)
     incubated = models.BooleanField(default=False)

     team = models.TextField()






     def __str__(self):
          #This provide the title to be the name shown to admin in databse
          return self.title
class remarks(models.Model): #remarks from the admin on the idea
     idea = models.ForeignKey(Idea, related_name="remarks", on_delete=models.CASCADE)  # it links logs with idea via ForeignKey
     body = models.TextField(blank=True)  # The is the remarks
     remarkdate: models.DateTimeField(auto_now_add=True)  # it records the date and time when the remark was added

     def __str__(self):
          return '%s - %s' % (self.idea.title,  self.body)

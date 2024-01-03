from django.db import models

# Create your models here.
class Topic(models.Model):
    topicname = models.CharField(max_length=10,primary_key=True)
    def __str__(self):
        return self.topicname
    
class Webpage(models.Model):
    topicname = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    url = models.URLField()
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    date = models.DateField()
    
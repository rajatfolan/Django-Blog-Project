from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Blog(models.Model):
    user=models.ForeignKey(User)
    created=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=20)
    image=models.FileField(null=True,blank=True)
    content=models.TextField(max_length=200)



    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=50)
    city = models.CharField(max_length=25,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    pic=models.FileField(default='pro.png')

    def __str__(self):
        return str(self.user)


def create_profile(sender , **kwargs ):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile , sender = User)

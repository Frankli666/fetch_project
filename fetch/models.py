'''Models for fetch app'''

'''django core imports'''
from django.db import models
from django.contrib.auth.models import User

#model for MasterUSer
class MasterUser(models.Model):
    #Links Django user to Master User
    user = models.OneToOneField(User)

    #Additional attributes to MasterUser
    picture = models.ImageField(upload_to='profile_images', blank=True)
    alt_email = models.EmailField(max_length=254)
    dob = models.DateField()

    MALE = 'M'
    FEMALE = 'F'
    GENDER_TYPE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1,
                                      choices=GENDER_TYPE,
                                      default=MALE)

    #gender = models.CharField(max_length=254)
    profession = models.CharField(max_length=254)
    address = models.TextField()
    mobile = models.IntegerField()
    landline = models.IntegerField()
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    nationality = models.CharField(max_length=254)
    language = models.CharField(max_length=254)

    def __unicode__(self):
        return self.user.username

class Sharer(MasterUser):
    '''sharer'''
    sharer_name = models.OneToOneField(MasterUser)

    def __unicode__(self):
        return self.sharer_name.username

class Getter(MasterUser):
    getter_name = models.OneToOneField(MasterUser)

    def __unicode__(self):
        return self.getter_name.username

class Connection(models.Model):
    ''' This class is about the  relationship status between users '''
    sourceUser = models.ForeignKey(Sharer)
    destUser = models.ForeignKey(Getter)
    conStatus = models.BinaryField()

    def __unicode__(self):
        return self.conStatus

"""
class Notification(models.Model):
    sender = models.CharField()
    receiver = models.CharField()
    notif_Detail = models.CharField() """

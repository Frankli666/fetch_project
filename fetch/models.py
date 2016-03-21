'''Models for fetch app'''

'''django core imports'''
from django.db import models
from django.contrib.auth.models import User
from actstream.models import Action
from django_model_changes import ChangesMixin
from django.template.defaultfilters import slugify


# model for MasterUSer
class MasterUser(ChangesMixin, models.Model):
    # Links Django user to Master User
    user = models.OneToOneField('auth.User', related_name='profile')

    # Additional attributes to MasterUser
    picture = models.ImageField(upload_to='profile_images', blank=True)
    alt_email = models.EmailField(default='', max_length=254)
    dob = models.DateField(null=True)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_TYPE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_TYPE,
                              default=MALE)

    # gender = models.CharField(max_length=254)
    profession = models.CharField(default='', max_length=10)
    address = models.TextField(default='')
    mobile = models.IntegerField(default=0)
    landline = models.IntegerField(default=0)
    city = models.CharField(default='', max_length=10)
    state = models.CharField(default='', max_length=10)
    country = models.CharField(default='', max_length=20)
    nationality = models.CharField(default='', max_length=10)
    language = models.CharField(default='', max_length=10)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(MasterUser, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: MasterUser.objects.get_or_create(user=u)[0])


class Sharer(ChangesMixin, models.Model):
    '''sharer'''
    sharer_name = models.ForeignKey(MasterUser, primary_key=True, related_name="sharer", )

    def __unicode__(self):
        return self.sharer_name.user.username


class Getter(ChangesMixin, models.Model):
    getter_name = models.ForeignKey(MasterUser, primary_key=True, related_name="getter")

    def __unicode__(self):
        return self.getter_name.user.username


class Connection(models.Model):
    ''' This class is about the  relationship status between users '''
    sourceUser = models.ForeignKey(Sharer)
    destUser = models.ForeignKey(Getter)
    conStatus = models.BinaryField()

    def __unicode__(self):
        return self.conStatus


class Notification(models.Model):
    user = models.ForeignKey(MasterUser, primary_key=True)
    action = models.ForeignKey(Action, default='')
    is_read = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.user.username

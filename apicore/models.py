from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Server(models.Model):
    hostname = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    port = models.CharField(max_length=5, null=True, blank=True)
    mac_address = models.CharField(max_length=150)
    volume = models.IntegerField(default=100)
    screen = models.BooleanField(default=True)
    pin = models.CharField(max_length=5)

    def __str__(self):
        return self.hostname

class ServerUser(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    session = models.CharField(max_length=250)
    connect_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session

class Extension(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# For custom upload functionally
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profiles/" + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        return self.user.username

# For signal use. Create a profile account when the User is created
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)
        print("Se ha creado el perfil para el usuario " + instance.username)

class FilesUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE)
    size = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Server(models.Model):
    hostname = models.CharField(max_length=200, verbose_name = 'Nombre del Servidor')
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=False, verbose_name = 'Dirección IP')
    port = models.CharField(max_length=5, null=True, blank=True, verbose_name = 'Puerto')
    mac_address = models.CharField(max_length=150, verbose_name = 'Dirección MAC')
    volume = models.IntegerField(default=100, verbose_name = 'Volumen')
    screen = models.BooleanField(default=True, verbose_name = 'Estado de Pantalla')
    pin = models.CharField(max_length=5, verbose_name = 'PIN de acceso')

    class Meta:
        verbose_name = 'servidor'
        verbose_name_plural = 'servidores'
        ordering = ['hostname']
    
    def __str__(self):
        return self.hostname

class ServerUser(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name = 'Servidor')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Usuario')
    status = models.BooleanField(default=True, verbose_name = 'Estado')
    session = models.CharField(max_length=250, verbose_name = 'Id de sesión')
    connect_date = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de conexión')
    last_date = models.DateTimeField(auto_now=True, verbose_name = 'Útima fecha de activdad')

    class Meta:
        verbose_name = 'sesión de usuario'
        verbose_name_plural = 'sesiones de usuario'
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

class Extension(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Nombre')
    status = models.BooleanField(default=True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'extension'
        verbose_name_plural = 'extensiones'
        ordering = ['name']

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=200, verbose_name = 'Nombre')
    status = models.BooleanField(default=True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'carrera'
        ordering = ['name']

    def __str__(self):
        return self.name

# For custom upload functionally
def custom_upload_to(instance, filename):
    old_instance = UserProfile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profiles/" + filename

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = 'Usuario')
    avatar = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, verbose_name = 'Avatar')
    career = models.ForeignKey(Career, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'Carrera')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ["user__username"]

    def __str__(self):
        return self.user.username

# For signal use. Create a profile account when the User is created
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        UserProfile.objects.get_or_create(user=instance)
        print("Se ha creado el perfil para el usuario " + instance.username)

# For custom upload functionally
def custom_upload_to_media(instance, filename):
    try:
        
        old_instance = FilesUser.objects.filter(pk=instance.pk)
        # old_instance.file.delete()
    except FilesUser.DoesNotExist:
        old_instance = None
    
    return "files/" + filename

class FilesUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    file = models.FileField(upload_to=custom_upload_to_media, blank=True, null=True, verbose_name = 'Archivo Multimedia')
    # extension = models.ForeignKey(Extension, on_delete=models.CASCADE)
    # size = models.IntegerField(blank=True, null=True)
    # path = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'archivo por usuario'
        verbose_name_plural = 'archivos por usuario'
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

class FileType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre')
    extensions = models.ManyToManyField(Extension, verbose_name="lista de extensiones")
    status = models.BooleanField(default=True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'Tipo de archivo'
        verbose_name_plural = 'Tipos de archivos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_extensions(self):
        return ", ".join([e.name for e in self.extensions.all()])

class CommandServer(models.Model):
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE, verbose_name = 'Tipo')
    action = models.CharField(max_length = 50, verbose_name = 'Acción')
    command = models.CharField(max_length = 200, verbose_name = 'Comando')
    status = models.BooleanField(default=True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'comando para ejecutar'
        verbose_name_plural = 'comandos para ejecutarse'
        ordering = ['action']

    def __str__(self):
        return self.action
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('El usuario debe tener un username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    def create_supervisorPSM(self, username, password=None, **extra_fields):
        """
        Creates and saves a supervisorPSM with the given username and password.
        """
        if not username:
            raise ValueError('El supervisorPSM debe tener un username')
        supervisorPSM = self.model(username=username)
        supervisorPSM.set_password(password)
        extra_fields.setdefault("is_staff", True)
        supervisorPSM.save(using=self._db)
        return supervisorPSM
    
    def create_admin(self, username, password=None, **extra_fields):
        """
        Creates and saves a admin with the given username and password.
        """
        if not username:
            raise ValueError('El Administrador debe tener un username')
        admin = self.model(username=username)
        admin.set_password(password)
        extra_fields.setdefault("is_staff", True)
        admin.save(using=self._db)
        return admin
    
class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        Userpage = 'USERPAGE', 'Userpage'
        SupervisorPSM = 'SUPERVISORPSM', 'Supervisorpsm'
        bossAdmin = 'BOSSADMIN', 'Bossadmin'
    
    type = models.CharField(_("Type"), max_length=256, choices=Types.choices, default=Types.Userpage
    )
    
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',  max_length=150, unique=True)
    email = models.EmailField('Email')
    first_names = models.CharField('First names',  max_length=150, blank=True)
    last_names = models.CharField('Last names',  max_length=150, blank=True)
    birth_date = models.DateField('Date of birth', auto_now=False, auto_now_add=False, max_length= 150, blank=True)
    type_identification = models.CharField('Type of identification',  max_length=150, blank=True)
    identification_num = models.BigIntegerField('Identification Number', unique=True, blank=True)
    password = models.CharField('Password',  max_length=150)
    testResult = models.BooleanField('test Result', default=True)
    isActive = models.BooleanField('is Active', default=True)
    
    #def #get_absolute_url(self):
        #return reverse("users:detail", kwargs={"username": self.username})
    
    def save(self, **kwargs):
        some_salt = 'uQIb8WdCT2fkelMOafzHjS'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'

class Userpage(User):
    class Meta:
        proxy=True

class Supervisorpsm(User):
    class Meta:
        proxy=True    

class bossAdmin(admin.ModelAdmin):
    pass        
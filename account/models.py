from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('User must have username!')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if password is None:
            raise TypeError('Superuser must have a password')

        user = self.create_user(
            username=username,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Country(models.Model):
    title = models.CharField(max_length=221)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)


class Company(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Account(AbstractBaseUser):
    TYPE = (
        (0, 'HR'),
        (1, 'Candidate'),
        (2, 'Staff'),
    )
    username = models.CharField(max_length=221, unique=True, verbose_name='username', db_index=True)
    first_name = models.CharField(max_length=221, verbose_name='first_name', null=True)
    last_name = models.CharField(max_length=221, verbose_name='last_name', null=True)
    avatar = models.ImageField(upload_to='account_avatar/')
    type = models.IntegerField(choices=TYPE, null=True, blank=True)
    bio = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    @property
    def image_url(self):
        if self.avatar:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.avatar.url}'
            return f'{settings.PROD_BASE_URL}{self.avatar.url}'
        return None


class WorkHistory(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    is_current = models.BooleanField(default=True)
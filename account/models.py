from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first name that can be validated (if requested) to eliminate '
                             'potential identity issues.')
        if not last_name:
            raise ValueError('Users must have a last name that can be validated (if requested) to eliminate potential '
                             'identity issues.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)  # REQUIRED BY DJANGO
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)  # REQUIRED BY DJANGO
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)  # REQUIRED BY DJANGO
    is_admin = models.BooleanField(default=False)  # REQUIRED BY DJANGO
    is_active = models.BooleanField(default=True)  # REQUIRED BY DJANGO
    is_staff = models.BooleanField(default=False)  # REQUIRED BY DJANGO
    is_superuser = models.BooleanField(default=False)  # REQUIRED BY DJANGO
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'  # Set this for what field you want the user to log in with!
    REQUIRED_FIELDS = ['username', "first_name", "last_name"]  # Fields you want required for registration

    objects = MyAccountManager()

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.username})"

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

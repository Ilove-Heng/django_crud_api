from django.db import models
# from django.utils import timezone
from datetime import date
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin



class MyUserManager(BaseUserManager):
    def create_user(self, email,name, date_of_birth,profile, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
            phone=phone,
            profile=profile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, date_of_birth,profile,phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            name=name,
            date_of_birth=date_of_birth,
            phone=phone,
            password=password,
            profile=profile,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    def profile_dir_path(instance, filename):
        ext = filename.split('.')[1]
        new_file_name = "users_profile/%s.%s" % ("profile_"+ str(instance.id),ext)
        return new_file_name


    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,

    )
    name=models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone= models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile = models.ImageField(upload_to=profile_dir_path, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone","date_of_birth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    class Meta:
        db_table='my_user'




class Task(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateField(default=date.today)
    created_by=models.ForeignKey(
        MyUser, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return "Task: " + self.name

    class Meta:
        db_table='task'
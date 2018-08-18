import uuid

from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    registration_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    home_phone_number = models.CharField(max_length=20, blank=True)
    mobile_phone_number = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, blank=True, null=True)
    user_type = 'generic'
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return 'User {} {}'.format(self.last_name, self.first_name)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

class Message(models.Model):
    GENERAL = 'GE'
    GREETING = 'GR'
    DISLIKE = 'DI'
    LIKE = 'LI'
    TOPIC_CHOICES = (
        (GENERAL,'General informations'),
        (GREETING, 'Greeting'),
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like'),
    )
    topic = models.CharField(
        max_length=2,
        choices=TOPIC_CHOICES,
        default=GENERAL,
    )
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        if len(self.content) > 20:
            return self.content[:19] + "..."
        else:
            return self.content


class Faculty(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=6)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return 'Name {}'.format(self.name)


class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    def __str__(self):
        return 'Name {}'.format(self.name)


class Job(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return 'Name {}'.format(self.title)


class Cursus(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Cursus'
        verbose_name_plural = 'Cursus'

    def __str__(self):
        return 'Name {}'.format(self.title)


class Employee(User):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    user_type = 'employee'

    def __str__(self):
        return 'Employee {}'.format(self.job.title)


class Student(User):
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    year = models.IntegerField()
    user_type = 'student'

    def __str__(self):
        return 'Student {}'.format(self.campus.name)


class Enterprise(User):
    logo = models.ImageField(upload_to='enterprise_image/%Y/%m/%d/', blank=True)
    office = models.CharField(max_length=30)
    address = models.TextField()
    user_type = 'enterprise'

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url

    def __str__(self):
        return 'Enterprise {}'.format(self.office)

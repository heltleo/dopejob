from django.db import models

# Create your models here.
class User(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length=20, blank=True)
    mobile_phone_number = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    user_type = 'generic'

    def __str__(self):
        return 'User {} {}'.format(self.last_name, self.first_name)

class Message(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        if len(self.content) > 20:
            return self.content[:19] + "..."
        else:
            return self.content


class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)

    def __str__(self):
        return 'Name {}'.format(self.name)


class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return 'Name {}'.format(self.name)


class Job(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return 'Name {}'.format(self.title)


class Cursus(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return 'Name {}'.format(self.title)


class Employee(User):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    user_type = 'employee'

    def __str__(self):
        return 'Job {}'.format(self.job.title)


class Student(User):
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    year = models.IntegerField()
    user_type = 'student'

    def __str__(self):
        return 'Job {}'.format(self.campus.name)

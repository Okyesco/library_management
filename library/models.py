from django.db import models
from django.utils import timezone


# Create your models here.

class Issuer(models.Model):
    objects = None
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class StudentRecord(models.Model):
    objects = None
    student_name = models.CharField(max_length=100, null=False)
    stage = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=10, null=False)
    book_name = models.TextField(max_length=10000, null=False)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='null')
    edition = models.CharField(max_length=30, default='null')
    return_date = models.DateField()
    date_borrowed = models.DateTimeField(default=timezone.now, blank=False)
    comment = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return f"'{self.student_name}' Has Borrowed '{self.book_name}'."


class StudentReturn(models.Model):
    objects = None
    student_name = models.CharField(max_length=100, null=False)
    stage = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=10, null=False)
    book_name = models.CharField(max_length=10000, null=False)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='null')
    edition = models.CharField(max_length=30, default='null')
    date_borrowed = models.DateTimeField(blank=False)
    return_date = models.DateTimeField(default=timezone.now, blank=False)
    comment = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return f"'{self.student_name}' Returned '{self.book_name}' on '{self.return_date}'"


class SchoolLogo(models.Model):
    objects = None
    logo = models.ImageField(upload_to='school_logo')


class LibraryShelve(models.Model):
    objects = None
    shelves = models.ImageField(upload_to='shelves_images')


class BorrowerImage(models.Model):
    objects = None
    borrower = models.ImageField(upload_to='borrower_image')


class TeachersReturn(models.Model):
    objects = None
    teacher_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=10)
    sex = models.CharField(max_length=10, null=False)
    book_name = models.TextField(max_length=10000, null=False)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='null')
    edition = models.CharField(max_length=30, default='null')
    date_borrowed = models.DateTimeField(blank=False)
    return_date = models.DateTimeField(default=timezone.now, blank=False)
    comment = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return f"'{self.teacher_name}' Returned '{self.book_name}' on '{self.return_date}'"


class TeachersRecord(models.Model):
    objects = None
    teacher_name = models.CharField(max_length=100, null=False)
    sex = models.CharField(max_length=10, null=False)
    phone_number = models.CharField(max_length=10)
    book_name = models.TextField(max_length=10000, null=False)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='null')
    edition = models.CharField(max_length=30, default='null')
    return_date = models.DateField()
    date_borrowed = models.DateTimeField(default=timezone.now, blank=False)
    comment = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return f"'{self.teacher_name}' Has Been Given '{self.book_name}'."


class TeacherImage(models.Model):
    objects = None
    teacher = models.ImageField(upload_to='teacher_image')

from datetime import date

from django.db import models


class Employee(models.Model):
    name = models.CharField(
        max_length=30,
    )
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )


class Department(models.Model):
    CITIES = [
        ("Sofia", "Sofia"),
        ("Plovdiv", "Plovdiv"),
        ("Burgas", "Burgas"),
        ("Varna", "Varna")
    ]
    code = models.CharField(
        max_length=4,
        unique=True,
        primary_key=True,
    )
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name="Employees Count"
    )
    location = models.CharField(
        max_length=20,
        choices=CITIES,
        null=True,
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    durations_in_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Duratione in Days",
    )
    estimated_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Estimated Hours",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
        default=date.today
    )
    crated_on = models.DateTimeField(
        editable=False,
        auto_now_add=True
    )
    last_edited_on = models.DateTimeField(
        editable=False,
        auto_now=True
    )
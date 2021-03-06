from django.db import models
from enum import Enum, unique
from django import forms
from django.contrib.auth.models import User
from .questions_enum import *
# Create your models here.


class BloodType(models.Model):

    @unique
    class Type(Enum):
        a = 0
        b = 1
        ab = 2
        o = 3

    TYPE_CHOICES = (
        (Type.a.value, "A"),
        (Type.b.value, "B"),
        (Type.ab.value, "AB"),
        (Type.o.value, "0")
    )

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)

    @unique
    class RHFactor(Enum):
        plus = True
        minus = False

    RH_CHOICES = (
        (RHFactor.plus.value, "+"),
        (RHFactor.minus.value, "-")
    )
    RH = models.BooleanField(choices=RH_CHOICES)

    def __str__(self):
        return self.get_type_display() + self.get_RH_display()


class Region(models.Model):

    @unique
    class Regions(Enum):
        Bratislavsky = 0
        Nitriansky = 1
        Trnavsky = 2
        Trenciansky = 3
        BanskoBystricky = 4
        Zilinsky = 5
        Kosicky = 6
        Presovsky = 7

    REGION_CHOICES = (
        (Regions.Bratislavsky.value, "Bratislavsky"),
        (Regions.Nitriansky.value, "Nitriansky"),
        (Regions.Trnavsky.value, "Trnavsky"),
        (Regions.BanskoBystricky.value, "BanskoBystricky"),
        (Regions.Zilinsky.value, "Zilinsky"),
        (Regions.Kosicky.value, "Kosicky"),
        (Regions.Presovsky.value, "Presovsky"),
        (Regions.Trenciansky.value, "Trenciansky")
    )

    name = models.PositiveSmallIntegerField(choices=REGION_CHOICES)


class Town(models.Model):
    name = models.CharField(max_length=255)
    id_region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    town = models.ForeignKey(
        Town, on_delete=models.SET_NULL, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=30, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)


class NTS(models.Model):
    name = models.CharField(max_length=30)
    id_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True)
    location_info = models.CharField(max_length=50, null=True)
    gps_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    other_contact = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    id_boss = models.IntegerField()
    secret_key = models.CharField(max_length=255, null=True)


class OfficeHours(models.Model):
    id_nts = models.ForeignKey(NTS, on_delete=models.CASCADE)
    DAYS_OF_WEEK = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    )
    day = models.SmallIntegerField(choices=DAYS_OF_WEEK)
    open_time = models.TimeField(blank=True)
    close_time = models.TimeField(blank=True)


class Announcement(models.Model):
    id_nts = models.ForeignKey(NTS, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)


class Employee(User):
    id_nts = models.ForeignKey(NTS, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=30, null=True)


class Donor(User):
    active_acount = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, null=True)
    personal_identification_number = models.DecimalField(
        max_digits=20, decimal_places=0)

    @unique
    class Gender(Enum):
        male = 0
        female = 1

    GENDER_CHOICES = (
        (Gender.female.value, 'female'),
        (Gender.male.value, 'male')
    )

    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=0)

    class Meta:
        unique_together = ('personal_identification_number',)


class DonorCard(Donor):
    name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    id_blood_type = models.ForeignKey(
        BloodType, on_delete=models.SET_NULL, null=True, blank=True)
    phone_num = models.CharField(max_length=20, blank=True)
    id_address_perm = models.ForeignKey(
        Address, on_delete=models.PROTECT, null=True, related_name="perm", blank=True)
    id_address_temp = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name="temp", blank=True)
    card_created_date = models.DateTimeField(auto_now_add=True, blank=True)
    card_created_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True)
    info = models.CharField(max_length=255, null=True, blank=True)
    can_donate_from = models.DateField(null=True, blank=True)


class Questionnaire(models.Model):
    id_donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    phone = models.CharField(max_length=20)
    created_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name="created")
    created_date = models.DateTimeField(auto_now_add=True)


class Questions(models.Model):

    @unique
    class Answer(Enum):
        yes = 1
        no = 0
        not_sure = 2

    ANSWER_CHOICES = (
        (Answer.no.value, 'no'),
        (Answer.yes.value, 'yes'),
        (Answer.not_sure.value, 'not sure')
    )

    question = models.PositiveSmallIntegerField(choices=QUESTION_CHOICES)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    answer = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES)
    additional_info = models.CharField(max_length=255, blank=True, null=True)
    employee_additional_info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('questionnaire', 'question')


class Booking(models.Model):
    id_nts = models.ForeignKey(NTS, on_delete=models.CASCADE)
    id_employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True)
    id_donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    id_answer_sheet = models.ForeignKey(
        Questionnaire, on_delete=models.SET_NULL, null=True)


class BloodExtraction(models.Model):

    @unique
    class State(Enum):
        new = 0
        ready_for_expedition = 1
        shipped = 2

    STATE_CHOICES = (
        (State.new.value, 'new'),
        (State.ready_for_expedition.value, 'ready for expedition'),
        (State.shipped.value, 'shipped')
    )

    state = models.PositiveSmallIntegerField(choices=STATE_CHOICES, default=0)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=255)
    id_donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    id_nts = models.ForeignKey(
        NTS, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    postpone = models.DateField(null=True, blank=True)
    note = models.CharField(max_length=255, blank=True)

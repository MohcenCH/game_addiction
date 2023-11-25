from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from main.managers import UserManager


class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addiction_level = models.CharField(max_length=255)
    average_hours_of_play_per_week = models.IntegerField()
    average_months_of_play = models.IntegerField()
    insomnia_score = models.IntegerField()
    excessive_sleepiness_score = models.IntegerField()
    anxiety_score = models.IntegerField()
    depression_score = models.IntegerField()


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    planned_therapy_sessions = models.IntegerField()


class Questionnaire(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_questionnaire = models.DateField()


class Question(models.Model):
    text_of_question = models.TextField()
    question_type = models.CharField(max_length=255)
    response_options = models.TextField()
    points_assigned_to_question = models.IntegerField()
    display_order_in_questionnaire = models.IntegerField()
    possible_question_dependencies = models.TextField()


class QuestionnaireResponse(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_to_question = models.TextField()
    score_assigned_to_response = models.IntegerField()
    comments_on_response = models.TextField()


class Alert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_alert = models.DateField()
    type_of_alert = models.CharField(max_length=255)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        User, related_name="recipient", on_delete=models.CASCADE
    )
    message_content = models.TextField()
    date_of_sending = models.DateTimeField()


class UsageStatistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_statistic = models.DateField()

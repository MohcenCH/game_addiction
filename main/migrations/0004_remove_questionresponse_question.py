# Generated by Django 4.2.7 on 2023-12-03 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_questionresponse_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionresponse',
            name='question',
        ),
    ]
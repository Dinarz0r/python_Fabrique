# Generated by Django 2.2.10 on 2021-06-18 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_questionnaire', '0003_auto_20210618_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmodel',
            name='type_question',
        ),
    ]

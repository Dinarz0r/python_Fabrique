# Generated by Django 2.2.10 on 2021-06-22 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_questionnaire', '0007_answermodel_many_option'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answermodel',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='answermodel',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='answermodel',
            name='answered_by',
        ),
        migrations.RemoveField(
            model_name='answermodel',
            name='questionText',
        ),
    ]
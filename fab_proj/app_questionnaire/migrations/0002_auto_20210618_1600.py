# Generated by Django 2.2.10 on 2021-06-18 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answermodel',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='pollmodel',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AlterModelOptions(
            name='questionmodel',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]

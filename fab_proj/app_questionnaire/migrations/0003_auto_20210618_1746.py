# Generated by Django 2.2.10 on 2021-06-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_questionnaire', '0002_auto_20210618_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='Выбор')),
            ],
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='start_date',
            field=models.DateTimeField(verbose_name='дата старта опрос'),
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='choice_answer',
            field=models.ManyToManyField(related_name='poll', to='app_questionnaire.OneQuestion', verbose_name='варианты ответов'),
        ),
    ]

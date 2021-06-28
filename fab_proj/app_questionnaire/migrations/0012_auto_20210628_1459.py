# Generated by Django 3.2.4 on 2021-06-28 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_questionnaire', '0011_auto_20210628_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='many_option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_questionnaire.optionquestionmodel', verbose_name='выбор одного'),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='option_question',
            field=models.ManyToManyField(blank=True, related_name='question_model', to='app_questionnaire.OptionQuestionModel', verbose_name='варианты ответов'),
        ),
    ]

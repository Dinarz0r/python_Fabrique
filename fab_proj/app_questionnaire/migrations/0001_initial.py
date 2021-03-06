# Generated by Django 2.2.10 on 2021-06-18 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(max_length=1000, verbose_name='описание')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name='дата старта опрос')),
                ('stop_date', models.DateTimeField(verbose_name='дата окончания опроса')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.TextField(max_length=100, verbose_name='текст вопроса')),
                ('type_question', models.CharField(choices=[('text', 'ответ текстом'), ('choice_one', 'ответ с выбором одного варианта'), ('choice_many', 'ответ с выбором нескольких вариантов')], max_length=11, verbose_name='тип опроса')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app_questionnaire.PollModel')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered_by', models.IntegerField()),
                ('answer_text', models.TextField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questionnaire.PollModel')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='app_questionnaire.QuestionModel')),
            ],
            options={
                'unique_together': {('poll', 'question', 'answered_by')},
            },
        ),
    ]

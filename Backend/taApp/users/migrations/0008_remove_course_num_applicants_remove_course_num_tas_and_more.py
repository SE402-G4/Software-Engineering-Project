# Generated by Django 5.0.6 on 2024-05-17 20:00

import django.db.models.deletion
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='num_applicants',
        ),
        migrations.RemoveField(
            model_name='course',
            name='num_tas',
        ),
        migrations.RemoveField(
            model_name='course',
            name='section',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='None', verbose_name='description'),
        ),
        migrations.AddField(
            model_name='course',
            name='minPoint',
            field=models.IntegerField(default=-1, verbose_name='minimum points'),
        ),
        migrations.AddField(
            model_name='course',
            name='passCourse',
            field=users.models.ZeroOrOneField(default=None, validators=[users.models.validate_zero_or_one], verbose_name='should pass'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Course Name'),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_year', models.IntegerField(verbose_name='sal vorodi')),
                ('field_of_study', models.CharField(max_length=70)),
                ('point', models.IntegerField(verbose_name='point of ta')),
                ('gpa', models.FloatField(verbose_name='moadele daneshjo')),
                ('status', models.CharField(choices=[('accept', 'Accept'), ('decline', 'Decline'), ('uncertain', 'Uncertain')], max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='users.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_id', to='users.studentprofile')),
            ],
        ),
    ]

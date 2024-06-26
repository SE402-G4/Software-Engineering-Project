# Generated by Django 5.0.3 on 2024-03-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professor",
            name="sts",
            field=models.ManyToManyField(
                related_name="professors",
                through="users.StudentProfessor",
                to="users.student",
                verbose_name="students",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="pros",
            field=models.ManyToManyField(
                related_name="students",
                through="users.StudentProfessor",
                to="users.professor",
                verbose_name="professors",
            ),
        ),
    ]

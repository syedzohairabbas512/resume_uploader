# Generated by Django 4.2.6 on 2023-10-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_resume", "0005_alter_resume_job_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="pin",
            field=models.PositiveIntegerField(),
        ),
    ]
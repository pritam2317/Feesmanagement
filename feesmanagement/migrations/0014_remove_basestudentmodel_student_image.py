# Generated by Django 4.0.3 on 2023-08-19 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feesmanagement', '0013_basestudentmodel_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basestudentmodel',
            name='student_image',
        ),
    ]

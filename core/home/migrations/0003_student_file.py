# Generated by Django 5.0.2 on 2024-02-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

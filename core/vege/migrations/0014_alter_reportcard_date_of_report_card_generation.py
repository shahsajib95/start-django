# Generated by Django 5.0.2 on 2024-02-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0013_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]

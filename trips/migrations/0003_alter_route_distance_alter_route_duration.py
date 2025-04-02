# Generated by Django 5.1.7 on 2025-04-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0002_trip_log_sheet_eldlog_route"),
    ]

    operations = [
        migrations.AlterField(
            model_name="route",
            name="distance",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="route",
            name="duration",
            field=models.FloatField(blank=True, null=True),
        ),
    ]

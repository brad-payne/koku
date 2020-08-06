# Generated by Django 2.2.14 on 2020-08-06 19:43
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0122_auto_20200803_2307")]

    operations = [
        migrations.AlterField(
            model_name="ocpusagelineitemdailysummary",
            name="infrastructure_project_raw_cost",
            field=models.DecimalField(decimal_places=15, default=0, max_digits=33),
        ),
        migrations.AlterField(
            model_name="ocpusagelineitemdailysummary",
            name="infrastructure_raw_cost",
            field=models.DecimalField(decimal_places=15, default=0, max_digits=33),
        ),
    ]

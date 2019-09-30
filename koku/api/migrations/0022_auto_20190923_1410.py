# Generated by Django 2.2.4 on 2019-09-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190917_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costmodelmetricsmap',
            name='source_type',
            field=models.CharField(choices=[('AWS', 'AWS'), ('OCP', 'OCP'), ('AZURE', 'AZURE'), ('GCP', 'GCP'), ('AWS-local', 'AWS-local'), ('AZURE-local', 'AZURE-local'), ('GCP-local', 'GCP-local')], max_length=50),
        ),
        migrations.AlterField(
            model_name='provider',
            name='type',
            field=models.CharField(choices=[('AWS', 'AWS'), ('OCP', 'OCP'), ('AZURE', 'AZURE'), ('GCP', 'GCP'), ('AWS-local', 'AWS-local'), ('AZURE-local', 'AZURE-local'), ('GCP-local', 'GCP-local')], default='AWS', max_length=50),
        ),
    ]
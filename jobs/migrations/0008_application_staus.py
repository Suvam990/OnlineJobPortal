# Generated by Django 5.1.7 on 2025-03-10 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_job_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='staus',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-20 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0014_remove_payments_studentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='StudentDetails',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inlingua_app.studentdetails'),
        ),
    ]

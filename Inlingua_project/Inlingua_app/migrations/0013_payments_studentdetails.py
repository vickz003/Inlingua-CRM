# Generated by Django 5.0.1 on 2024-01-19 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0012_paymentmethod_remove_payments_transactionstatusid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='StudentDetails',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inlingua_app.studentdetails'),
        ),
    ]

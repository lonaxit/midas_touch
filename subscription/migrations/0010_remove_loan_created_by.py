# Generated by Django 4.0.1 on 2022-03-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0009_loan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='created_by',
        ),
    ]

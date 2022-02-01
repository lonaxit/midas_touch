# Generated by Django 4.0.1 on 2022-02-01 10:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('reference', models.CharField(max_length=200)),
                ('applied_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('approved_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('monthly_deduction', models.DecimalField(decimal_places=2, max_digits=20)),
                ('net_pay', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tenor', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(36)])),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loan', to='subscription.product')),
            ],
        ),
    ]
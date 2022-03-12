# Generated by Django 4.0.1 on 2022-03-08 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_loan_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_user',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='product',
        ),
        migrations.RemoveField(
            model_name='loandeduction',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='loandeduction',
            name='loan',
        ),
        migrations.RemoveField(
            model_name='loandeduction',
            name='loandeduction_user',
        ),
        migrations.RemoveField(
            model_name='loandeductionsummary',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='ConsolidatedLoan',
        ),
        migrations.DeleteModel(
            name='Loan',
        ),
        migrations.DeleteModel(
            name='LoanDeduction',
        ),
        migrations.DeleteModel(
            name='LoanDeductionSummary',
        ),
    ]
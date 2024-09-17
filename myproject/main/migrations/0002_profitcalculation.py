# Generated by Django 4.2 on 2024-09-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=100)),
                ('weekly_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cg_regular_weekly_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cg_weekly_ot_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cg_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('case_monthly_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cg_regular_monthly_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cg_monthly_ot_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('select_rbs', models.CharField(max_length=50)),
                ('reimbursement_county', models.CharField(max_length=100)),
                ('select_modifier', models.CharField(choices=[('UA', 'UA'), ('UB', 'UB'), ('UC', 'UC')], max_length=10)),
                ('select_rate_code', models.CharField(max_length=10)),
                ('monthly_reimbursement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insurance_pay_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insurance_pay_rate_reimb', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hourly_pay_with_rbs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cg_regular_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cg_ot_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_cg_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cg_payment_plus_22', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

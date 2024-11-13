# Generated by Django 3.2.6 on 2024-10-11 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.company')),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('widget_type', models.CharField(choices=[('total_revenue', 'Общая выручка'), ('variable_expenses', 'Переменные расходы'), ('fixed_expenses', 'Постоянные расходы'), ('operating_profit', 'Операционная прибыль (EBITDA)'), ('net_profit', 'Чистая прибыль за период'), ('operational_profit_margin', 'Рентабельность по операционной прибыли, %'), ('debtor_liability', 'Дебиторская задолженность'), ('creditor_liability', 'Кредиторская задолженность'), ('turnover_days_debtors', 'Оборочиваемость д.з. (дни)'), ('turnover_days_creditors', 'Оборочиваемость к.з. (дни)'), ('cash_flow', 'Операционный денежный поток (OCF)')], max_length=50)),
                ('position', models.IntegerField()),
                ('data', models.TextField(blank=True, null=True)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.dashboard')),
            ],
        ),
    ]
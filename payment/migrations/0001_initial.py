# Generated by Django 3.0.6 on 2020-05-26 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0007_auto_20200526_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_fees', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('our_fees', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('is_paid', models.BooleanField(default=False)),
                ('task_deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal_transaction', to='tasks.TaskDeal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

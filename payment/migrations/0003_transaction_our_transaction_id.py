# Generated by Django 3.0.6 on 2020-05-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20200526_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='our_transaction_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

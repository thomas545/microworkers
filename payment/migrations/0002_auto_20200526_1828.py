# Generated by Django 3.0.6 on 2020-05-26 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name_plural': 'Transactions'},
        ),
    ]
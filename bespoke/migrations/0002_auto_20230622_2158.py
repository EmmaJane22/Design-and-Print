# Generated by Django 3.2.19 on 2023-06-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bespoke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bespokeorder',
            name='accept_quote',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='bespokeorder',
            name='quote',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]

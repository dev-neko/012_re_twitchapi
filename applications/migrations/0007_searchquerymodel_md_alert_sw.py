# Generated by Django 3.1.7 on 2021-04-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_auto_20210408_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_alert_sw',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
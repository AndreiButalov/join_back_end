# Generated by Django 5.2.1 on 2025-06-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0024_remove_usercontact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontact',
            name='plain_password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]

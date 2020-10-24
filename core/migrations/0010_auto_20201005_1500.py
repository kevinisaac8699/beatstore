# Generated by Django 2.2.4 on 2020-10-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_verifiedbeat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='rate',
        ),
        migrations.AddField(
            model_name='beat',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='VerifiedBeat',
        ),
    ]
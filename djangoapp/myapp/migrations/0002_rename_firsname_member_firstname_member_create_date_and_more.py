# Generated by Django 5.1.1 on 2024-09-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='firsname',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='member',
            name='create_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]

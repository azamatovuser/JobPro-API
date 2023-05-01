# Generated by Django 4.2 on 2023-05-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.IntegerField(choices=[(0, 'HR'), (1, 'Candidate'), (2, 'Staff')], default=1),
            preserve_default=False,
        ),
    ]
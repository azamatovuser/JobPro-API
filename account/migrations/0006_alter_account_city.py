# Generated by Django 4.2 on 2023-05-06 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='account.city'),
        ),
    ]

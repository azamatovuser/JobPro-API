# Generated by Django 4.2 on 2023-04-27 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('description', models.TextField()),
                ('deadline', models.CharField(max_length=221)),
                ('salary', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('types', models.IntegerField(choices=[(0, 'Full time'), (1, 'Part time'), (2, 'Freelance'), (3, 'Internship'), (4, 'Temporary')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.position')),
            ],
        ),
    ]
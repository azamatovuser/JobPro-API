# Generated by Django 4.2 on 2023-04-28 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_type_remove_job_types_job_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='active',
            new_name='is_active',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.company'),
            preserve_default=False,
        ),
    ]

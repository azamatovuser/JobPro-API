# Generated by Django 4.2 on 2023-05-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_author_alter_wishlist_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='cv_file/')),
                ('message', models.TextField()),
            ],
        ),
    ]

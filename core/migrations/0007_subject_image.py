# Generated by Django 4.2 on 2024-04-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_subject_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subjects/'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_alter_inquiry_inquiry_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='inquiry_status',
            field=models.CharField(choices=[('register', 'Register'), ('register_complete', 'Register Complete'), ('complete', 'Complete')], max_length=20),
        ),
    ]

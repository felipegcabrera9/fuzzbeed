# Generated by Django 2.2 on 2020-02-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20200214_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(default='1988-08-12'),
            preserve_default=False,
        ),
    ]

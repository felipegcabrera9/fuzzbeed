# Generated by Django 2.2 on 2020-02-25 19:43

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0003_user_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='quiz_banner')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('o1', models.CharField(max_length=50)),
                ('o2', models.CharField(max_length=50)),
                ('o3', models.CharField(max_length=50)),
                ('o4', models.CharField(max_length=50)),
                ('qna', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fuzzbeed_app.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='users',
            field=models.ManyToManyField(through='fuzzbeed_app.Result', to='login_app.User'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-02 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_author_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='icon',
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='What_you_learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
    ]

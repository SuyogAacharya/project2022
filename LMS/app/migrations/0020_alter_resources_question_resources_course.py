# Generated by Django 5.0.2 on 2024-03-10 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_resources_course_remove_subtopic_quiz_topic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources_question',
            name='Resources_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.resources_course'),
        ),
    ]

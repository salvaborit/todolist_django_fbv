# Generated by Django 4.1.4 on 2023-01-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_task_urgency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='base.tag'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['title', 'description'], name='base_task_title_7b2191_idx'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('1', 'Doing'), ('2', 'Done')], max_length=1),
        ),
    ]

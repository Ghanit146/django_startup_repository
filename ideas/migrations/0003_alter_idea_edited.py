# Generated by Django 3.2 on 2021-11-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='edited',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
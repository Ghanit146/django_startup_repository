# Generated by Django 3.2 on 2021-12-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_idea_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='logs',
            field=models.TextField(blank=True),
        ),
    ]

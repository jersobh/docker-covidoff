# Generated by Django 3.0.4 on 2020-03-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Announcement content', max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text='Creation date')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='Last update')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Todo_title', models.CharField(max_length=50)),
                ('Todo_description', models.CharField(max_length=100)),
                ('Todo_status', models.BooleanField(default=False)),
            ],
        ),
    ]

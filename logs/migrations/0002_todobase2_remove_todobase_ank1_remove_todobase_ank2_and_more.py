# Generated by Django 4.0.5 on 2022-06-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoBase2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ank1', models.TextField()),
                ('ank2', models.TextField()),
                ('ank3', models.TextField()),
                ('ank4', models.TextField()),
                ('ank5', models.TextField()),
                ('ank6', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='todobase',
            name='ank1',
        ),
        migrations.RemoveField(
            model_name='todobase',
            name='ank2',
        ),
        migrations.RemoveField(
            model_name='todobase',
            name='ank3',
        ),
        migrations.RemoveField(
            model_name='todobase',
            name='ank4',
        ),
        migrations.RemoveField(
            model_name='todobase',
            name='ank5',
        ),
        migrations.RemoveField(
            model_name='todobase',
            name='ank6',
        ),
    ]

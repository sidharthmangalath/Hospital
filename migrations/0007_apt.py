# Generated by Django 5.0.4 on 2024-05-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0006_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='apt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pmob', models.CharField(max_length=100)),
                ('pmail', models.CharField(max_length=100)),
                ('pdate', models.CharField(max_length=100)),
                ('pdpt', models.CharField(max_length=100)),
                ('pdtr', models.CharField(max_length=100)),
                ('paddr', models.CharField(max_length=100)),
            ],
        ),
    ]

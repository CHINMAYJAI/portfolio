# Generated by Django 5.1.3 on 2024-11-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=122)),
                ('reason_to_contact', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]

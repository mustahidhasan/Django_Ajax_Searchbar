# Generated by Django 3.2.6 on 2021-08-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_board_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_name', models.TextField()),
                ('uni_category', models.TextField()),
                ('uni_url', models.TextField()),
            ],
        ),
    ]

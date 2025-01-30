# Generated by Django 5.1.4 on 2025-01-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0004_alter_car_options_alter_carbrand_options_and_more'),
        ('home_app', '0008_alter_about_options_alter_promovideo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLuxuryCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Eng Top mashinalar')),
                ('cars', models.ManyToManyField(to='car_app.car', verbose_name='Mashinalar')),
            ],
            options={
                'verbose_name': 'Eng Top mashina',
                'verbose_name_plural': 'Eng Top mashinalar',
            },
        ),
    ]

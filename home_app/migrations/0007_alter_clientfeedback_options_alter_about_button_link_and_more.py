# Generated by Django 5.1.4 on 2025-01-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_contactpage_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientfeedback',
            options={'ordering': ['-id'], 'verbose_name': 'Mijoz fikri', 'verbose_name_plural': 'Mijoz fikrlari'},
        ),
        migrations.AlterField(
            model_name='about',
            name='button_link',
            field=models.CharField(max_length=255, verbose_name='Tugma havolasi'),
        ),
        migrations.AlterField(
            model_name='about',
            name='cap_title',
            field=models.CharField(max_length=255, verbose_name='Bosh sarlavha'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about_pics/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='about',
            name='one_text',
            field=models.CharField(max_length=255, verbose_name='Birinchi matn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='about',
            name='two_text',
            field=models.CharField(max_length=255, verbose_name='Ikkinchi matn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='video',
            field=models.TextField(verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='clientfeedback',
            name='feedback',
            field=models.TextField(verbose_name='Fikr'),
        ),
        migrations.AlterField(
            model_name='clientfeedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='client_images/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='clientfeedback',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='clientfeedback',
            name='rating',
            field=models.IntegerField(default=5, verbose_name='Reyting'),
        ),
        migrations.AlterField(
            model_name='clientfeedback',
            name='who',
            field=models.CharField(max_length=255, verbose_name='Kimligi'),
        ),
        migrations.AlterField(
            model_name='promovideo',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='promovideo',
            name='video',
            field=models.TextField(verbose_name='Video'),
        ),
    ]

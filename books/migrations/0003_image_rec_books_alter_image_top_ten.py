# Generated by Django 4.1.3 on 2022-11-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='rec_books',
            field=models.ImageField(null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='image',
            name='top_ten',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]
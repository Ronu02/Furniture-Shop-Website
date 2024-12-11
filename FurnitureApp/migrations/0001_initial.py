# Generated by Django 5.1.2 on 2024-10-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Category_description', models.TextField(blank=True, max_length=300, null=True)),
                ('Category_image', models.ImageField(blank=True, null=True, upload_to='Category_Images')),
            ],
        ),
    ]

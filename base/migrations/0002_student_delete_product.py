# Generated by Django 5.1.1 on 2024-09-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sName', models.CharField(max_length=20)),
                ('age', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

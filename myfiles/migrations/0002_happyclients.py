# Generated by Django 4.1.2 on 2022-10-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappyClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma', models.CharField(max_length=150)),
                ('rasim', models.ImageField(upload_to='media')),
                ('ism', models.CharField(max_length=20)),
                ('lavozim', models.CharField(max_length=50)),
            ],
        ),
    ]
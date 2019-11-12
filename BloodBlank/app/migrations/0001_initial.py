# Generated by Django 2.1.5 on 2019-11-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DonorLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('d_uname', models.CharField(max_length=30)),
                ('d_pwd', models.CharField(max_length=30)),
                ('gender', models.BooleanField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField(max_length=30)),
                ('bloodgroup', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('age', models.IntegerField(max_length=30)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lastdonationdate', models.DateField()),
            ],
        ),
    ]
# Generated by Django 2.2 on 2020-12-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('desc', models.TextField()),
                ('author', models.CharField(max_length=60)),
            ],
        ),
    ]

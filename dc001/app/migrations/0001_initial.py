# Generated by Django 3.1.5 on 2022-08-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(db_index=True)),
                ('category', models.SlugField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=128)),
                ('firstParagraph', models.TextField()),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=32, unique=True)),
                ('picture', models.CharField(max_length=256)),
            ],
        ),
    ]

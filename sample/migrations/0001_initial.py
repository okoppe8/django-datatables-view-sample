# Generated by Django 2.1.3 on 2018-12-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_name', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=10)),
                ('furigana', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=12)),
                ('code', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'サンプル',
                'verbose_name_plural': 'サンプル',
            },
        ),
    ]

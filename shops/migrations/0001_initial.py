# Generated by Django 5.0.3 on 2024-03-19 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]

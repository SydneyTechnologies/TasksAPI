# Generated by Django 4.1.4 on 2022-12-23 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('0a9fd1cd-3493-45ac-a73a-e41e2c9023e8'), primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('completed', models.IntegerField(default=0)),
                ('total_tasks', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.collections')),
            ],
            options={
                'verbose_name': 'Task',
            },
        ),
    ]

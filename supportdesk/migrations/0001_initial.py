# Generated by Django 4.0.3 on 2022-03-15 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('summary', models.CharField(default=None, max_length=127)),
                ('description', models.CharField(default=None, max_length=511)),
                ('is_high_priority', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to_user', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

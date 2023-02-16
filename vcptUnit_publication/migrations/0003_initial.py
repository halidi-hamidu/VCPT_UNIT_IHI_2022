# Generated by Django 4.0.4 on 2023-02-16 08:23

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vcptUnit_publication', '0002_delete_vcptupublications'),
    ]

    operations = [
        migrations.CreateModel(
            name='VcptuPublications',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('publication_year', models.PositiveIntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publcation_content_posted_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'VCPTU-Publications',
            },
        ),
    ]

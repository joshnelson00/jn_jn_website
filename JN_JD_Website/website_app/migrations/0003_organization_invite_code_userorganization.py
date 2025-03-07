# Generated by Django 5.1.5 on 2025-02-16 01:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0002_userevents'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='invite_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='UserOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(db_column='Organization_ID', on_delete=django.db.models.deletion.CASCADE, related_name='user_organizations', to='website_app.organization')),
                ('user', models.ForeignKey(db_column='User_ID', on_delete=django.db.models.deletion.CASCADE, related_name='user_organizations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

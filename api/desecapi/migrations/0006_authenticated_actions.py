# Generated by Django 2.2.1 on 2019-09-21 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('desecapi', '0005_user_model_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticatedAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.PositiveIntegerField(default=lambda: int(datetime.timestamp(timezone.now())))),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthenticatedUserAction',
            fields=[
                ('authenticatedaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='desecapi.AuthenticatedAction')),
            ],
            options={
                'managed': False,
            },
            bases=('desecapi.authenticatedaction',),
        ),
        migrations.CreateModel(
            name='AuthenticatedActivateUserAction',
            fields=[
                ('authenticateduseraction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='desecapi.AuthenticatedUserAction')),
                ('domain', models.CharField(max_length=191)),
            ],
            options={
                'managed': False,
            },
            bases=('desecapi.authenticateduseraction',),
        ),
        migrations.CreateModel(
            name='AuthenticatedChangeEmailUserAction',
            fields=[
                ('authenticateduseraction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='desecapi.AuthenticatedUserAction')),
                ('new_email', models.EmailField(max_length=254)),
            ],
            options={
                'managed': False,
            },
            bases=('desecapi.authenticateduseraction',),
        ),
        migrations.CreateModel(
            name='AuthenticatedDeleteUserAction',
            fields=[
                ('authenticateduseraction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='desecapi.AuthenticatedUserAction')),
            ],
            options={
                'managed': False,
            },
            bases=('desecapi.authenticateduseraction',),
        ),
        migrations.CreateModel(
            name='AuthenticatedResetPasswordUserAction',
            fields=[
                ('authenticateduseraction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='desecapi.AuthenticatedUserAction')),
                ('new_password', models.CharField(max_length=128)),
            ],
            options={
                'managed': False,
            },
            bases=('desecapi.authenticateduseraction',),
        ),
    ]

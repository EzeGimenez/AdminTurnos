# Generated by Django 3.0.6 on 2020-05-23 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20200523_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Job',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobtype',
            fields=[
                ('type', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'JobType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('type', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Notification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('serviceprovider_owner_id', models.BigIntegerField()),
                ('street', models.CharField(max_length=30)),
                ('streetnumber', models.IntegerField()),
                ('apnumber', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('businessname', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Place',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promoapplied',
            fields=[
                ('service_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'promoApplied',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('since', models.DateField()),
                ('to', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('days', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Promotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serviceproviderauth',
            fields=[
                ('serviceprovider', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Serviceprovider')),
                ('email', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'ServiceProviderAuth',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='serviceprovider',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Clientauth',
            fields=[
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Client')),
                ('email', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'ClientAuth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Placedoes',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Place')),
            ],
            options={
                'db_table': 'PlaceDoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prefers',
            fields=[
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Client')),
                ('contact_info', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Prefers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promoincludes',
            fields=[
                ('promotion', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Promotion')),
                ('discount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'promoIncludes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provides',
            fields=[
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Job')),
                ('day', models.IntegerField()),
                ('cost', models.FloatField()),
                ('duration', models.TimeField()),
                ('day_start', models.TimeField()),
                ('day_end', models.TimeField()),
                ('pause_start', models.TimeField(blank=True, null=True)),
                ('pause_end', models.TimeField(blank=True, null=True)),
                ('parallelism', models.IntegerField()),
            ],
            options={
                'db_table': 'Provides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serviceinstance',
            fields=[
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rest.Appointment')),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'ServiceInstance',
                'managed': False,
            },
        ),
    ]

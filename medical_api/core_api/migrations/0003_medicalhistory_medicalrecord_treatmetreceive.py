# Generated by Django 3.1.5 on 2021-01-26 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0002_auto_20210126_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='in kg')),
                ('blood_pressure', models.CharField(max_length=10)),
                ('temperature', models.IntegerField(help_text='in celsius')),
                ('pulse_rate', models.IntegerField()),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='citizen_medical', to='core_api.citizenpersonalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentReceive',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(max_length=400)),
                ('medical_rec', models.ManyToManyField(related_name='treatment_record',
                                                       to='core_api.MedicalRecord', verbose_name='treatment record')),
            ],
            options={
                'verbose_name_plural': 'Treatment Received',
            },
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=400)),
                ('medical_rec', models.ManyToManyField(related_name='medical_history',
                                                       to='core_api.MedicalRecord', verbose_name='medical record')),
            ],
            options={
                'verbose_name_plural': 'Medical Histories',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_auto_20170403_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenchMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('bar_type', models.CharField(blank=True, max_length=60)),
                ('floor', models.BooleanField()),
                ('reverse', models.BooleanField()),
                ('standard', models.BooleanField()),
                ('board', models.BooleanField()),
                ('manpon', models.BooleanField()),
                ('pin', models.BooleanField()),
                ('notes', models.CharField(blank=True, max_length=60)),
                ('bands', models.CharField(blank=True, max_length=60)),
                ('chains', models.CharField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeadliftMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('sumo_conventional', models.CharField(max_length=60)),
                ('deficit', models.BooleanField()),
                ('block', models.BooleanField()),
                ('standard', models.BooleanField()),
                ('pin', models.BooleanField()),
                ('reverse', models.BooleanField()),
                ('movement_weight', models.IntegerField(default=0)),
                ('movement_reps', models.IntegerField(default=0)),
                ('deadlift_notes', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LowerAccessoryMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('chair_dl', models.CharField(blank=True, max_length=60)),
                ('ghr', models.CharField(blank=True, max_length=60)),
                ('lunge', models.CharField(blank=True, max_length=60)),
                ('dimel_dl', models.CharField(blank=True, max_length=60)),
                ('reverse_hyper', models.CharField(blank=True, max_length=60)),
                ('hip_bridge', models.CharField(blank=True, max_length=60)),
                ('good_morning', models.CharField(blank=True, max_length=60)),
                ('step_up', models.CharField(blank=True, max_length=60)),
                ('belt_squat', models.CharField(blank=True, max_length=60)),
                ('hack_squat', models.CharField(blank=True, max_length=60)),
                ('leg_press', models.CharField(blank=True, max_length=60)),
                ('leg_curl', models.CharField(blank=True, max_length=60)),
                ('stiff_leg_dl', models.CharField(blank=True, max_length=60)),
                ('inverse_curl', models.CharField(blank=True, max_length=60)),
                ('front_squat', models.CharField(blank=True, max_length=60)),
                ('back_extension', models.CharField(blank=True, max_length=60)),
                ('top_set', models.CharField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SquatMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('effort_type', models.CharField(max_length=60)),
                ('box_free', models.CharField(max_length=60)),
                ('bar_type', models.CharField(blank=True, max_length=60)),
                ('bands_type', models.CharField(blank=True, max_length=60)),
                ('chain_weight', models.IntegerField(blank=True, default=0)),
                ('movement_weight', models.IntegerField(default=0)),
                ('movement_reps', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UpperAccessoryMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('top_set', models.CharField(blank=True, max_length=60)),
                ('close_grippness', models.CharField(blank=True, max_length=60)),
                ('tate_press', models.CharField(blank=True, max_length=60)),
                ('dips', models.CharField(blank=True, max_length=60)),
                ('rev_db_fly', models.CharField(blank=True, max_length=60)),
                ('windmills', models.CharField(blank=True, max_length=60)),
                ('bamboo_bar', models.CharField(blank=True, max_length=60)),
                ('lat_pulldowns', models.CharField(blank=True, max_length=60)),
                ('lat_pullovers', models.CharField(blank=True, max_length=60)),
                ('pec_dec', models.CharField(blank=True, max_length=60)),
                ('reverse_pec_dec', models.CharField(blank=True, max_length=60)),
                ('t_bar_rows', models.CharField(blank=True, max_length=60)),
                ('chest_supported_rows', models.CharField(blank=True, max_length=60)),
                ('low_rows', models.CharField(blank=True, max_length=60)),
                ('pullups', models.CharField(blank=True, max_length=60)),
                ('inverted_row', models.CharField(blank=True, max_length=60)),
                ('face_pulls', models.CharField(blank=True, max_length=60)),
                ('db_rows', models.CharField(blank=True, max_length=60)),
                ('db_press', models.CharField(blank=True, max_length=60)),
                ('pullaparts', models.CharField(blank=True, max_length=60)),
                ('tri_extensions', models.CharField(blank=True, max_length=60)),
                ('skull_crushers', models.CharField(blank=True, max_length=60)),
                ('jam_press', models.CharField(blank=True, max_length=60)),
                ('olt_press', models.CharField(blank=True, max_length=60)),
                ('db_rollbacks', models.CharField(blank=True, max_length=60)),
                ('dead_press', models.CharField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
# Generated by Django 2.2 on 2019-12-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WHOLifeExpectancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('GHO', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('Global', 'Global'), ('Africa', 'Africa'), ('Americas', 'Americas'), ('South-East Asia', 'South-East Asia'), ('Europe', 'Europe'), ('Eastern Mediterranean', 'Eastern Mediterranean'), ('Western Pacific', 'Western Pacific')], max_length=30)),
                ('year', models.PositiveIntegerField(default=2019)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both sexes', 'Both sexes')], max_length=10)),
                ('number_of_years', models.FloatField()),
            ],
            options={
                'unique_together': {('region', 'year', 'GHO', 'sex')},
            },
        ),
    ]